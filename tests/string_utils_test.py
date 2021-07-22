from lib.string_utils import char_count, offset_char


def test_should_return_character_count_from_text():
    result = char_count('Hello')

    assert len(result) == 4
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def test_should_return_string_by_offsetting_characters():
    assert offset_char('owl', 3) == 'rzo'
    assert offset_char('mammoth', 7) == 'thttvao'

def test_should_return_string_by_offsetting_characters_by_starting_over_if_goes_beyond_z():
    result = offset_char('xz', 2)
    
    assert result == 'zb'
