from lib.kingdom import Kingdom
from typing import Dict, Optional


class Kingdoms:
    kingdom_dict: Dict[str, Kingdom]

    def __init__(self):
        self.kingdom_dict = {}

    def add_kingdom(self, name: str, emblem: str):
        self.kingdom_dict[name.upper()] = Kingdom(name, emblem)

    def find_by_name(self, name: str) -> Optional[Kingdom]:
        return None if name == None else self.kingdom_dict.get(name.upper())
