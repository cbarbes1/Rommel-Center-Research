from abc import ABC, abstractmethod
from fuzzywuzzy import fuzz, process

class SimilarityStrategy(ABC):
    @abstractmethod
    def check_similarity(self, names):
        pass