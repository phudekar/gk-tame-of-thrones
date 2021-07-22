from typing import List
from input_parser import parse_line
from lib.kingdoms import Kingdoms, Kingdom
import sys

kingdom_of_shan = 'SPACE'

kingdoms = Kingdoms()
kingdoms.add_kingdom(kingdom_of_shan, 'Gorilla')
kingdoms.add_kingdom('LAND', 'Panda')
kingdoms.add_kingdom('WATER', 'Octopus')
kingdoms.add_kingdom('ICE', 'Mammoth')
kingdoms.add_kingdom('AIR', 'Owl')
kingdoms.add_kingdom('FIRE', 'Dragon')


def find_ruler(lines: List[str]) -> str:
    allies = []
    for line in lines:
        parsed_line = parse_line(line)
        kingdom = kingdoms.find_by_name(parsed_line.kingdom)
        if parsed_line.kingdom != kingdom_of_shan \
            and parsed_line.kingdom != None \
            and kingdom != None \
            and kingdom.is_ally(parsed_line.message):
            allies.append(parsed_line.kingdom)
    return 'NONE' if len(allies) < 3 else kingdom_of_shan + ' ' + ' '.join(allies)

def main():
    filename = sys.argv[1]
    lines = open(filename, mode ='+r').readlines()
    print(find_ruler(lines))


if __name__ == '__main__':
    main()
