from lib.kingdoms import Kingdoms

def test_should_return_none_if_kingdom_is_not_present():
    kingdoms =  Kingdoms()
    
    space =kingdoms.find_by_name('SPACE')
    
    assert space == None
    
def test_should_return_kingdom_from_name():
    kingdoms =  Kingdoms()
    kingdoms.add_kingdom('SPACE', 'Gorilla')
    
    space =kingdoms.find_by_name('SPACE')
    
    assert space != None
    assert space.name == 'SPACE'
    assert space.emblem == 'Gorilla'

