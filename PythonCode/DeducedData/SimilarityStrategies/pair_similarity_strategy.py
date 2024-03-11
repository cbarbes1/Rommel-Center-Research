from DeducedData.SimilarityStrategy import SimilarityStrategy
from itertools import combinations
from fuzzywuzzy import fuzz, process

class PairSimilarityStrategy(SimilarityStrategy):
    @staticmethod
    def check_similarity(SimilarityStrategy, names: list[str]):
        pairs = combinations(names, 2)
        for item1, item2 in pairs:
            # Extract the first names and consider only up to the first space (if present)
            first_name1 = item1.split(", ")[1].split(" ")[0] if ", " in item1 else ''
            first_name2 = item2.split(", ")[1].split(" ")[0] if ", " in item2 else ''
            
            # Check if the first letters of the first names match and compare the lengths of the first names
            if first_name1[0] == first_name2[0] and len(first_name1) == len(first_name2):
                similarity = fuzz.ratio(item1, item2)  

