from dataclasses import dataclass
from lib.string_utils import char_count, offset_char


@dataclass
class Kingdom:
    name: str
    emblem: str

    def is_ally(self, message: str) -> bool:
        return self.contains_emblem(message)

    def contains_emblem(self, message: str) -> bool:
        emblem_chars = char_count(self.encrypted_emblem())
        message_chars = char_count(message)

        for e in emblem_chars.keys():
            if message_chars.get(e) == None \
                    or message_chars.get(e) < emblem_chars.get(e):
                return False

        return True

    def encrypted_emblem(self) -> str:
        offset = len(self.emblem)
        return offset_char(self.emblem, offset)
