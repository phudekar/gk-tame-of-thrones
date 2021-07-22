from lib.kingdom import Kingdom
from input_parser import parse_line


def test_should_parse_input():
    message = 'FDIXXSOKKOFBBMU'
    kingdom = 'LAND'
    result = parse_line(kingdom + ' ' + message)

    assert result.kingdom == kingdom
    assert result.message == message

def test_should_parse_invalid_input():
    result = parse_line(' ')

    assert result.kingdom == None
    assert result.message == None
