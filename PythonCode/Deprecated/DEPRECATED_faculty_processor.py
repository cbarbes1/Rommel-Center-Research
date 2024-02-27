import re
import Levenshtein
import copy
import random

class FacultyPreprocessor:
    def __init__(self):
        # Initialize the original author name as an empty string
        self.original_author_name = ""
        
        # Compiled regex patterns to save on computation time
        # Pattern to remove middle initial from author name
        self.middle_initial_pattern = re.compile(r'\s+[A-Z]\.\s*')
        # Pattern to remove whitespace from author name
        self.name_compressor_pattern = re.compile(r'\s+')
        
        # Dictionary to hold compressed names and original names
        # Key: compressed name (str), Value: original name (str)
        self.author_names_dict = {}
    
    def get_original_name(self, compressed_name):
        """
        Retrieves the original name for a given compressed name.
        
        Args:
            compressed_name (str): The compressed name to look up.
        
        Returns:
            tuple: (bool, str) A tuple where the first element is True if the original name was found,
                   and False otherwise. The second element is the original name or an error message.
        """
        try:
            return True, self.author_names_dict[compressed_name]
        except KeyError:
            return False, f"Original name for {compressed_name} not found. KeyError"
    
    def save_original_author_name(self, original_author_name):
        """
        Saves the provided author name as the current original author name.
        
        Args:
            original_author_name (str): The full name of the author.
        """
        self.original_author_name = original_author_name

    def remove_middle_intial(self, author_name):
        """
        Removes the middle initial from the authors name if present
        
        Args:
            author_name (str): Full name of author
        
        Returns:
            (str): The author's name with the middle initial removed
        """
        # Use MI Pattern to remove middle intial from any names that have them
        return self.middle_initial_pattern.sub('', author_name)
    
    def name_compressor(self, author_name):
        """
        Compresses the author's name by removing whitespace and converting the name to lowercase
        
        Args:
            author_name (str): The name of the author to be compressed
        Returns:
            str: The compressed author name
        """
        return self.name_compressor_pattern.sub('', author_name).lower()
    
    def name_smusher(self, author_name):
        """
        Processes the author's name by removing the middle initial and compressing the name
        Updates the author names dictionary with the transformed name as the key and original name as the value
        
        Args:
            author_name (str): The name of the author to be processed
        
        Returns:
            str: 
        """
        self.save_original_author_name(author_name)
        compressed_name = self.remove_middle_intial(author_name)
        compressed_name = self.name_compressor(compressed_name)
        
        # Add/ Update dictionary: author_names_dict with compressed name as key and original name as value
        self.author_names_dict[compressed_name] = self.original_author_name
        return compressed_name

    def get_authors_dict(self):
        return self.author_names_dict
        
class FacultyPostprocessor:
    def __init__(self):
        self.temp_dict = {}
        self.faculty_occurence_dict = {}
        self.processed_sets_list = []
        self.faculty_preprocessor = FacultyPreprocessor()
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
        
    def occurence_counter(self, faculty_sets):
        for faculty_set in faculty_sets:
            for faculty in faculty_set:
                if faculty in self.faculty_occurence_dict:
                    self.faculty_occurence_dict[faculty] += 1
                    continue
                else:
                    self.faculty_occurence_dict[faculty] = 1
         
    
    def filter_names_by_initials(self, author_set):
        """
        Filters each set of faculty names, keeping only those where the first letter of both the first and last name
        match the first letter of the original author name.
        
        Args:
            author_sets (dict): A list of sets of author names.
        
        Returns:
            
        """
        # TODO: implement
        filtered_set = {name for name in author_set if len(name.split()) >= 2 and name.split()[0][0].lower() == name.split()[-1][0].lower()}
        return filtered_set
    
    def remove_near_duplicates(self, category_dict):
        #TODO: Implement
        """
        Controls the flow of the class calling neccesary function to handle the edge case of near duplicates slipping through
        preprocessing.
        """
        self.temp_dict = copy.deepcopy(category_dict)
        
        # list of all faculty sets
        faculty_sets = self.extract_faculty_sets(self.temp_dict)
        
        # Iterate through each category and faculty set
        for category, faculty_set in self.temp_dict.items():
            filtered_set = self.filter_names_by_initials(faculty_set)
            final_set = self.duplicate_postprocessor(filtered_set, faculty_sets)
            
            # Update original dict with processed set (right now a temp dict)
            self.temp_dict[category]['faculty_set'] = final_set
            
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
        
        
        
    def duplicate_postprocessor1(self, faculty_set, faculty_sets, similarity_threshold=0.5):
        """
        Detects near-duplicate names within a single set of filtered names (faculty_set) and identifies
        which version of each near-duplicate name is most common across all sets in faculty_sets.
        
        Args:
            faculty_set (set): A set of filtered names, names that possessed the same initials.
            faculty_sets (list): A list of all the sets of author names.
       
        Returns:
            set: A set of author names after removing near duplicates.
        """
        name_signatures = {}
        
        # Generate MinHash signatures for each name in faculty_set
        for name in faculty_set:
            tokens = self.minhash_util.tokenize(string=name, n=3)
            signature = self.minhash_util.compute_signature(tokens)
            name_signatures[name] = signature
        
        # Initialize a dict to count occurences of each name variant across all sets
        name_occurences = {name: 0 for name in faculty_set}
        
        final_decision = {}
        
        count = 0
        # Identify near-duplicates within faculty_set
        print(f'FACULTY SET\n {faculty_set}\n\n')
        print(f'FACULTY SETS\n {faculty_sets}\n\n')
        #to_remove = set()
        for name1, signature1 in name_signatures.items():
            #print("for loop 1\n")
            #print(f'NAME1:\n{name1}\n')
            #print(f"SIGNATURE1:\n{signature1}\n")
            for name2, signature2 in name_signatures.items():
                #print(f'NAME1:\n{name2}\n')
                #print(f"SIGNATURE1:\n{signature2}\n")
                #print("for loop 2\n")
                if name1 != name2: # Avoid comparing name with itself
                    #print("if 1\n")
                    similarity = self.minhash_util.compare_signatures(signature1=signature1, signature2=signature2)
                    if similarity > similarity_threshold:
                        #print("if 2\n")
                        # Count occurences of each name in all faculty_sets
                        count1 = sum(name1 in f_set for f_set in faculty_sets)
                        count2 = sum(name2 in f_set for f_set in faculty_sets)
                        
                        if count1 < count2: # name 2 occurs more get rid of name 1
                            final_decision[name1] = 'remove'
                            final_decision.setdefault(name2, 'keep')
                            print(f'LOOP NUM: {count}')
                            print(f'ADDED NAME1: {name1} TO REMOVE SET\n')
                        elif count1 > count2: # name 1 occurs more get rid of name 2
                            final_decision[name2] = 'remove'
                            final_decision.setdefault(name1, 'keep')
                            print(f'LOOP NUM: {count}')
                            print(f'ADDED NAME2: {name2} TO REMOVE SET\n')
                        # elif count1 == count2 and len(faculty_set) > 2: # name 1 and 2 are equal, keep 1 discard 2
                        #     to_remove.add(name2)
                        #     processed_names.add(name1)
                        #     print(f'LOOP NUM: {count}')
                        #     print(f'EQUAL: ADDED NAME2: {name2} TO REMOVE SET\n')
                        count += 1
                        #print(f"IN LOOP TO REMOVE\n{to_remove}\n")
        #print(f'TO REMOVE SET\n {to_remove}\n\n')
        # Remove less common near-duplicate from faculty_set
        to_remove = {name for name, decision in final_decision.items() if decision == 'remove'}
        refined_set = set(name_signatures) - to_remove
        print(f"REFINED SET\n{refined_set}")
        # Covert remaining names back to their original form
        #original_names_set = {self.faculty_preprocessor.get_original_name(name)[1] for name in refined_set}
        #print(f"ORIGINAL NAMES SET\n{original_names_set}\n")
        
        return refined_set
                                
            
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
        
    """
    POSSIBLE IMPLEMENTATION
    TODO: CHECK THE LOGIC
    
        def remove_near_duplicates(self, category_dict):
        
        Controls the flow of the class, calling necessary functions to handle the edge case of near duplicates slipping through
        preprocessing.
        
        Args:
            category_dict (dict): A dictionary where the keys are category names and the values are sets of faculty names.
        
        faculty_sets = self.get_sets_from_dict(category_dict)
        for category, author_set in category_dict.items():
            filtered_set = self.filter_names_by_initials(author_set)
            final_set = self.process_for_duplicates(filtered_set, faculty_sets)
            # Update the original category_dict with the processed set
            category_dict[category] = final_set

    def process_for_duplicates(self, author_set, faculty_sets):
        
        Processes a set of author names to remove near duplicates, keeping the most frequently occurring name across all sets.
        
        Args:
            author_set (set): A set of author names to process.
            faculty_sets (list): A list of all sets of author names.
        
        Returns:
            set: A set of author names after removing near duplicates.
        
        all_names = set().union(*faculty_sets)  # Combine all names from all sets
        final_set = set()
        for name in author_set:
            similar_names = {other_name for other_name in all_names if Levenshtein.distance(name, other_name) <= 2}
            most_frequent_name = max(similar_names, key=lambda x: sum(x in s for s in faculty_sets))
            final_set.add(most_frequent_name)
        return final_set
    """