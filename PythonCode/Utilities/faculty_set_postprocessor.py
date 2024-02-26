import copy
import random

        
class FacultyPostprocessor:
    def __init__(self):
        self.temp_dict = {}
        self.faculty_occurence_dict = {}
        self.processed_sets_list = []
        self.minhash_util = MinHashUtility(num_hashes=100)

    def get_temp_dict(self):
        return self.temp_dict
    
    def extract_faculty_sets(self, category_dict):
        #TODO: Implement
        """
        Extracts the faculty_set value from each key in category_dict and stores those lists in a set
        
        Args:
            category_dict (dictionary): A dictionary where the keys are the category names and the values contain a faculty_set. 
        Returns:
            list_of_faculty_sets (list): A list containing each set from all the keys in category_dict
        """
        list_of_faculty_sets = []
        
        for key in category_dict:
            try:
                list_of_faculty_sets.append(category_dict[key]['faculty_set'])
            except:
                print(f"Error extracting faculty sets from {key}, continuing to next")
        return list_of_faculty_sets
    
    # def remove_near_duplicates(self, category_dict):
    #     """
    #     Controls the flow of the class calling neccesary function to handle the edge case of near duplicates slipping through
    #     preprocessing.
    #     """
    #     print(f"\n\n\n\nIN NEAR DUPLICATES\n{category_dict}\n\n")
    #     self.temp_dict = copy.deepcopy(category_dict)
    #     print(f'\n\n\n\nTEMP DICT IN NEAR DUPLICATE\n{self.temp_dict}\n\n')
    #     # list of all faculty sets
    #     faculty_sets = self.extract_faculty_sets(self.temp_dict)
        
    #     # Iterate through each category and faculty set
    #     for category, faculty_set in self.temp_dict.items():
    #         final_set = self.duplicate_postprocessor(faculty_set, faculty_sets)
            
    #         # Update original dict with processed set (right now a temp dict)
    #         self.temp_dict[category]['faculty_set'] = final_set       
    #     return self.temp_dict
    
    def remove_near_duplicates(self, category_dict):
        # self.temp_dict = copy.deepcopy(category_dict)
        # faculty_sets = self.extract_faculty_sets(self.temp_dict)
        # final_set = self.duplicate_postprocessor(self.temp_dict['faculty_set'], faculty_sets)
        # self.temp_dict['faculty_set'] = final_set
        # return self.temp_dict
        self.temp_dict = copy.deepcopy(category_dict)
        if 'faculty_set' in self.temp_dict:
            faculty_sets = self.extract_faculty_sets(self.temp_dict['faculty_set'])
            final_set = self.duplicate_postprocessor(self.temp_dict['faculty_set'], faculty_sets)
            self.temp_dict['faculty_set'] = final_set
        return self.temp_dict
        
    def duplicate_postprocessor(self, faculty_set, faculty_sets, similarity_threshold=0.5):
        # Step 1: Generate MinHash signatures for all names
        name_signatures = {}
        all_names = set().union(*faculty_sets) # Combine all names from all sets
        for name in all_names:
            tokens = self.minhash_util.tokenize(name)
            signature = self.minhash_util.compute_signature(tokens)
            name_signatures[name] = signature
        
        # Step 2: Compare signatures and decide which names to keep
        to_remove = set()
        names_list = list(name_signatures.keys())
        
        # Get occurence frequency of each name across all faculty sets
        name_frequency = {name: sum(name in f_set for f_set in faculty_sets) for name in all_names}
        
        for i in range(len(names_list)):
            for j in range(i+1, len(names_list)):
                name1, name2 = names_list[i], names_list[j]
                signature1, signature2 = name_signatures[name1], name_signatures[name2]
                
                # Compare signatures
                similarity = self.minhash_util.compare_signatures(signature1, signature2)
                if similarity > similarity_threshold:
                    if name_frequency[name1] > name_frequency[name2] or (name_frequency[name1] == name_frequency[name2] and name1 < name2):
                        to_remove.add(name2)
                    else:
                        to_remove.add(name1)
                        
        refined_fac_set = [f_set - to_remove for f_set in faculty_sets]
        print(f"\n\n\n\n\n****REFINED FAC SET 2****\n{refined_fac_set}\n\n\n\n")
        return refined_fac_set
            
class MinHashUtility:
    def __init__ (self, num_hashes):
        self.num_hashes = num_hashes
        self.large_prime = 999983 # large prime number used for hashing
        self.hash_fns = self.generate_hash_functions()
        
    def tokenize(self, string, n=3):
        """
        Tokenize the string into n-grams. 
        Helps identify similar strings even if they aren't of the same length or composition.
        
        More on n-grams: https://en.wikipedia.org/wiki/N-gram
        
        Args:
            string (str): The string to tokenize.
            n (int): The length of each n-gram.
            
        Returns:
            set: A set of n-grams from the input string.
        """
        # Using set to ensure unique n-grams
        return set(string[i:i+n] for i in range(len(string)-n+1))

    def generate_hash_functions(self):
        """
        Generate a list of linear hash functions.
        Each function is defined by a unique pair of coefficients (a, b).
        Ensures diverse set of hash functions for MinHash comparison.
        
        Overview of hash functions: https://en.wikipedia.org/wiki/Hash_function
        
        Returns:
            list: A list of lambda functions which represent the hash functions.
        """
        def _hash_factory(a, b):
            # Defines a hash function with coefficients a, b
            return lambda x: (a * x + b) % self.large_prime
        
        hash_fns = []
        for _ in range(self.num_hashes):
            a = random.randint(1, self.large_prime - 1)
            b = random.randint(0, self.large_prime - 1)
            hash_fns.append(_hash_factory(a, b))
        return hash_fns

    def compute_signature(self, tokens):
        """
        Compute MinHash signature for a set of tokens.
        Signature consists of the minimum hash value produced by each hash function across all tokens.
        
        Detailed explanation of MinHash and its computation: https://en.wikipedia.org/wiki/MinHash
        
        Args:
            tokens (set): A set of tokens to compute the MinHash signature for.
            
        Returns:
            list: A list of minimum hash values, representing the MinHash signature.
        """
        signature = [float('inf')] * self.num_hashes
        for token in tokens:
            #print(f"TOKEN:\n{token}\n")
            hashed_values = [hash_fn(hash(token)) for hash_fn in self.hash_fns]
            for i in range (self.num_hashes):
                signature[i] = min(signature[i], hashed_values[i])
        #print(f"FINAL SIGNATURE:\n{signature}\n")
        return signature
    
    def compare_signatures(self, signature1, signature2):
        """
        Compare two MinHash signatures and return their similarity.
        The similarity is the fraction of positions at which the two signatures have the same value,
        esitimating the Jaccard similarity of the original sets.
        
        More on estimating similarity with MinHash: https://en.wikipedia.org/wiki/Jaccard_index#MinHash
        
        Args:
            signature1 (list): The MinHash signature of the first set.
            signature2 (list): The MinHash signature of the second set.
        
        Returns:
            float: The estimated similarity between the two sets, based on their MinHash signatures.
        """
        assert len(signature1) == len(signature2), "Signatures must be of the same length | compare_signatures() in MinHashUtility class." 
        matching = sum(1 for i, j in zip(signature1, signature2) if i == j)
        similarity = matching / len(signature1)
        #print(f"CALCULATED SIMILARITY:\n{similarity}\n")
        return similarity