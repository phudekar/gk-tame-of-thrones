from typing import Dict

def char_range(a, b):
    for c in range(ord(a), ord(b)+1):
        yield chr(c)

def char_count(text: str) -> Dict[str, int]:
    result = {}
    for char in text:
        count = result.get(char.lower())
        result[char.lower()] = count + 1 if count != None else 1
    return result


def offset_char(text: str, offset: int) -> str:
    chars = list(char_range('a','z'))
    result = ""
    for char in text:
        index = chars.index(char.lower()) + offset
        if(index > len(chars)):
            index = index - len(chars)
        result += chars[index]
    return result
