from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class CitationData:
    journel: str = ""
    journal_ranking: str = ""
    number_of_citations: int = 0
    
    number_of_publications: int = 0
    citation_list: Dict = field(default_factory=dict)

@dataclass
class TopicData:
    topic: str = ""
    Citation: List = field(default_factory=list)
    total_publication: int = 0
    total_citations: int = 0

@dataclass
class faculty_info:
    name: str = ""
    type: str = ""
    department: str = ""
    phone: str = ""
    mail: str = ""
    website: str = ""