from lib.kingdom import Kingdom
from dataclasses import dataclass

@dataclass
class ParsedLine:
    kingdom: str
    message: str

def parse_line(text:str) -> ParsedLine:
    split =  text.strip().split(' ')
    kingdom = split[0] if len(split) > 0 and len(split[0]) > 0 else None
    message = ''.join(split[1:]) if len(split) > 1 else None
    return ParsedLine(kingdom, message)