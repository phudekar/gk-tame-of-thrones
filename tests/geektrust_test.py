from geektrust import find_ruler


def test_should_find_ruler():
    lines = """
    AIR ROZO
    LAND FAIJWJSOOFAMAU
    ICE STHSTSTVSASOS
    """.splitlines()
    assert find_ruler(lines) == 'SPACE AIR LAND ICE'


def test_should_find_ruler_case_1():
    lines = """
     LAND FDIXXSOKKOFBBMU
     ICE MOMAMVTMTMHTM
     WATER SUMMER IS COMING
     AIR OWLAOWLBOWLC
     FIRE AJXGAMUTA
    """.splitlines()
    assert find_ruler(lines) == 'SPACE LAND ICE FIRE'

   

def test_should_find_no_ruler():
    lines="""
    AIR OWLAOWLBOWLC
    LAND OFBBMUFDICCSO
    ICE VTBTBHTBBBOBAB
    WATER SUMMER IS COMING
    """
    assert find_ruler(lines) == 'NONE'
