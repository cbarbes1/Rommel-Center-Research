import copy
import random
from typing import List
from dataclasses import dataclass, field
from typing import Dict


class FacultyPostprocessor:
    def __init__(self):
        self.temp_dict = {}
        self.faculty_occurence_dict = {}
        self.processed_sets_list = []
        self.minhash_util = MinHashUtility(num_hashes=100)

    def get_temp_dict(self):
        return self.temp_dict

    def extract_faculty_sets(self, category_dict):
        """
        Extracts the faculty attribute from each CategoryInfo object in categories

        Args:
            categories (iterable of CategoryInfo): An iterable containing CategoryInfo objects.
        Returns:
            list_of_faculty_sets (list): A list containing the faculty set from each CategoryInfo object
        """
        list_of_faculty_sets = [
            category_info.faculty for category_info in category_dict.values()
        ]
        return list_of_faculty_sets

    def remove_near_duplicates(self, category_dict):
        """
        Processes each CategoryInfo object to remove near-duplicate faculty names based on MinHash similarity.

        Args:
            categories (iterable of CategoryInfo): An iterable containing CategoryInfo objects.
        Returns:
            None: The method directly modifies the faculty attribute of each CategoryInfo object.
        """
        faculty_sets_list: list[set] = self.extract_faculty_sets(
            category_dict=category_dict
        )
        for category, category_info in category_dict.items():
            final_set = self.duplicate_postprocessor(
                category_info.faculty, faculty_sets_list
            )
            category_info.faculty = final_set
        
        # Extract the updated faculty sets after duplicate removal
        updated_faculty_sets = self.extract_faculty_sets(category_dict=category_dict)

        # Standardize names across all sets based on the most frequent global variation
        standardized_sets = self.standardize_names_across_sets(updated_faculty_sets)

        # Update the category_dict with standardized faculty sets
        for (category, category_info), standardized_set in zip(category_dict.items(), standardized_sets):
            category_info.faculty = standardized_set
        
        return category_dict

    def duplicate_postprocessor(
        self, faculty_set, faculty_sets, similarity_threshold=0.5
    ):
        
        # Generate the most frequent name variation mapping
        most_frequent_variation = self.get_most_frequent_name_variation(faculty_sets)
        
        # Step 1: Generate MinHash signatures for all names in the faculty_set
        name_signatures = {
            name: self.minhash_util.compute_signature(self.minhash_util.tokenize(name))
            for name in faculty_set
        }

        # Step 2: Prepare to track names to removed based on comparisons
        to_remove: set = set()

        # Step 3: Compare each name against all others in the set for near duplicates
        for n1 in faculty_set:
            for n2 in faculty_set:
                if n1 != n2:
                    signature1 = name_signatures[n1]
                    signature2 = name_signatures[n2]
                    similarity = self.minhash_util.compare_signatures(
                        signature1, signature2
                    )

                    # If similarity exceeds threshold, determine which name to keep
                    if similarity > similarity_threshold:
                        # Determine occurence frequency of each name across all faculty sets
                        #n1_freq = sum(n1 in f_set for f_set in faculty_sets)
                        #n2_freq = sum(n2 in f_set for f_set in faculty_sets)

                        n1_normalized = n1.lower().replace(" ", "")
                        n2_normalized = n2.lower().replace(" ", "")
                        
                        if most_frequent_variation[n1_normalized] == n1 and most_frequent_variation[n2_normalized] != n2:
                            to_remove.add(n2)
                        elif most_frequent_variation[n2_normalized] == n2 and most_frequent_variation[n1_normalized] != n1:
                            to_remove.add(n1)
                        else:
                            if n1 < n2:
                                to_remove.add(n2)
                            else:
                                to_remove.add(n1)
                        # Keep the name that occurs more frequently, schedule the other for removal
#                         if n1_freq > n2_freq:
#                             to_remove.add(n2)
#                         elif n2_freq > n1_freq:
#                             to_remove.add(n1) """
#                         # If frequencies are equal
# """                         elif n1 < n2:
#                             to_remove.add(n2)
#                         else:
#                             to_remove.add(n1)
        # Step 4: Refine the faculty_set by removing identified less frequent duplicates
        refined_fac_set = faculty_set - to_remove

        return refined_fac_set
    
    def get_most_frequent_name_variation(self, faculty_sets_list):
        name_variations: dict = {}
        
        for faculty_set in faculty_sets_list:
            for name in faculty_set:
                normalized_name = name.lower().replace(" ", "")
                if normalized_name not in name_variations:
                    name_variations[normalized_name] = NameVariation(normalized_name)
                name_variations[normalized_name].add_variation(name)
                
        # Extract the most frequent variation for each normalized name.
        most_frequent_variation = {normalized_name: variation.most_frequent_variation() 
                                   for normalized_name, variation in name_variations.items()}
        
        return most_frequent_variation
    
    def standardize_names_across_sets(self, faculty_sets_list):
        # First, generate the most frequent name variation mapping across all sets
        most_frequent_variation = self.get_most_frequent_name_variation(faculty_sets_list)

        # Then, iterate through each set and standardize names based on the global mapping
        standardized_sets = []
        for faculty_set in faculty_sets_list:
            standardized_set = set()
            for name in faculty_set:
                normalized_name = name.lower().replace(" ", "")
                # Replace the name with its most frequent variation, if available
                standardized_name = most_frequent_variation.get(normalized_name, name)
                standardized_set.add(standardized_name)
            standardized_sets.append(standardized_set)

        return standardized_sets


class MinHashUtility:
    def __init__(self, num_hashes):
        self.num_hashes = num_hashes
        self.large_prime = 999983  # large prime number used for hashing
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
        return set(string[i : i + n] for i in range(len(string) - n + 1))
    
    def generate_coeeficients(self):
        coefficients = []
        for _ in range(self.num_hashes):
            a = random.randint(1, self.large_prime - 1)
            b = random.randint(0, self.large_prime - 1)
            coefficients.append((a, b))
        return coefficients

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
        # for a, b in self.generate_coeeficients:
        #     hash_fns.append(lambda x: (a * x + b) % self.large_prime)
        
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
        signature = [float("inf")] * self.num_hashes
        for token in tokens:
            hashed_values = [hash_fn(hash(token)) for hash_fn in self.hash_fns]
            for i in range(self.num_hashes):
                signature[i] = min(signature[i], hashed_values[i])
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
        assert len(signature1) == len(
            signature2
        ), "Signatures must be of the same length | compare_signatures() in MinHashUtility class."
        matching = sum(1 for i, j in zip(signature1, signature2) if i == j)
        similarity = matching / len(signature1)
        return similarity

@dataclass
class NameVariation:
    normalized_name: str
    variations: Dict[str, int] = field(default_factory=dict)
    
    def add_variation(self, variation: str):
        if variation in self.variations:
            self.variations[variation] += 1
        else:
            self.variations[variation] = 1
        
    def most_frequent_variation(self):
        return max(self.variations, key=self.variations.get)

