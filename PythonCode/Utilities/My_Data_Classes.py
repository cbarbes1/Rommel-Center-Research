from dataclasses import dataclass, field
from typing import Set

@dataclass
class CategoryInfo:
    faculty_count: int = 0
    department_count: int = 0
    files: Set[str] = field(default_factory=set)
    faculty: Set[str] = field(default_factory=set)
    departments: Set[str] = field(default_factory=set)
    article_set: Set[str] = field(default_factory=set)

