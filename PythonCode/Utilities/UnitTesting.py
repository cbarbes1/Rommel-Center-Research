import unittest
import json
#from PythonCode.Utilities.DEPRECATED_faculty_processor import MinHashUtility, FacultyPostprocessor, FacultyPreprocessor
from faculty_set_postprocessor import FacultyPostprocessor, MinHashUtility
class TestMinHashUtility(unittest.TestCase):
    def setUp(self):
        self.minhash_util = MinHashUtility(num_hashes=100)
        
    def test_tokenization(self):
        string = "doe,john"
        expected_ngrams = {'doe', ',jo', 'oe,', 'ohn', 'e,j', 'joh'}
        ngrams = self.minhash_util.tokenize(string, n=3)
        self.assertEqual(ngrams, expected_ngrams)
        
    def test_signature_comparisoin(self):
        name1 = "doe,john"
        name2 = "doe,johnmiddlename"
        tokens1 = self.minhash_util.tokenize(name1, n=8)
        tokens2 = self.minhash_util.tokenize(name2, n=8)
        signature1 = self.minhash_util.compute_signature(tokens1)
        signature2 = self.minhash_util.compute_signature(tokens2)
        self.assertTrue(all(isinstance(num, (int, float)) for num in signature1), "Signature1 contains non-numeric values")
        self.assertTrue(all(isinstance(num, (int, float)) for num in signature2), "Signature2 contains non-numeric values")
        similarity = self.minhash_util.compare_signatures(signature1, signature2)
        self.assertTrue(0 < similarity <= 1) # expect some similarity but not necessarily 1

def test_duplicate_postprocessor():
    # Intialize the necessary processors
    fac_pre = FacultyPreprocessor()
    fac_post = FacultyPostprocessor()
    
    # Sample sets of names, including near-duplicates
    faculty_sets = [
        {"Doe, John", "Doe, Sophie", "Gang, Kwangwook"},
        {"Gang, Kwangwook", "Gang, KwangWook", "Gang, Kwang Wook"},
        {"Tu, Junyi", "Tu, Junyi M.", "Wang, Sophie"},
    ]

    all_compressed_sets = []
    # Process names to simulate preprocessing steps
    for faculty_set in faculty_sets:
        #print(f"FACULTY SET LOOP LN44:\n{faculty_set}\n")
        compressed_set = {fac_pre.name_smusher(name) for name in faculty_set}
        #print(f'COMPRESSED SET:\n {compressed_set}\n\n')
        author_dict = fac_pre.get_authors_dict()
        #print(f"SAVED NAMES DICT:\n{json.dumps(author_dict)}\n")
        all_compressed_sets.append(compressed_set)
    
    #print(f"\n\n\nALL COMPRESSED SETS\n{all_compressed_sets}\n\n\n")
    
#     # Process each set
#     for compressed_set in all_compressed_sets:
#         print(f"IN LOOP PROCESSING COMPRESSED SET:\n{compressed_set}\n")
#         fac_post.temp_dict["Sample Category"] = {"faculty_set": compressed_set}
#         # Apply duplicate post processing
#         fac_post.duplicate_postprocessor(compressed_set, all_compressed_sets)
#         print(fac_post.temp_dict)
        
#         # Retrieve and print processed sets
#         processed_sets = fac_post.temp_dict["Sample Category"]["faculty_set"]
#         original_names_set = {fac_pre.get_original_name(name)[1] for name in processed_sets}
        
#         print(f"COMPRESSED SET PROCESSED\n {compressed_set}\n")
#         print(f"PROCESSED SETS:\n {processed_sets}\n\n")
#         print(f"ORIGINAL NAMES SET\n {original_names_set}")
        
    # Process each set
    for faculty_set in faculty_sets:
        print(f"IN LOOP PROCESSING FACULTY SET:\n{faculty_set}\n")
        fac_post.temp_dict["Sample Category"] = {"faculty_set": faculty_set}
        # Apply duplicate post processing
        fac_post.duplicate_postprocessor(faculty_set, faculty_sets)
        #print(fac_post.temp_dict)
        
        # Retrieve and print processed sets
        #processed_sets = fac_post.temp_dict["Sample Category"]["faculty_set"]
        #original_names_set = {fac_pre.get_original_name(name)[1] for name in processed_sets}
        
        #print(f"FACULTY SET PROCESSED\n {faculty_set}\n")
        #print(f"PROCESSED SETS:\n {processed_sets}\n\n")
        #print(f"ORIGINAL NAMES SET\n {original_names_set}")

def test_faculty_post():
    # Step 1: Load JSON object into a dict
    with open('categories_and_category_metadata.json', 'r') as file:
        data = json.load(file)
    
    category_data = data["Management"]
    print(category_data)
    postprocessor = FacultyPostprocessor()
    refined_data = postprocessor.remove_near_duplicates(category_data)
    #print(f"REFINED DATA\n{refined_data}\n")
    return refined_data

if __name__ == '__main__':
    unittest.main(exit=False)
    data = test_faculty_post()
    print(data)
