#!/usr/bin/env python3

import cursor
import os
import argparse

parser = argparse.ArgumentParser(prog='Mapper', usage='%(prog)s [opciones]')
parser.add_argument('-c', '--city', type=str, nargs='+', help='loc')
args = parser.parse_args()
ubic = args.city

ubi = ''.join(ubic)
#print('∷∷{}∷∷{}'.format(ubi))

#PID = os.popen("ps -d | grep -E 'term' | awk '{print $1}'").readline()
#TERM = os.popen(f"ps -o 'comm=' -p {PID}").readlines()
#print(TERM)

def selector(uno):
	lugares = {
	'Rusia': ['\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷'],
	'Canada': ['∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷'],
	'Francia': ['∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷'],
	'Alemania': ['∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷','∷','∷','∷'],
	'España': ['∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷','∷','∷'],
	'United States': ['∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷','∷'],
	'China': ['∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷','∷'],
	'Mexico': ['∷','∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷','∷'],
	'India': ['∷','∷','∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷','∷'],
	'Peru': ['∷','∷','∷','∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷','∷'],
	'Brasil': ['∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷','∷'],
	'Chile': ['∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m','∷'],
	'Argentina': ['∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','∷','\033[6;31mX\033[;0m'],
	}
	return lugares.get(uno)

selected = selector(ubi)
#print('∷∷{}∷∷{}∷∷{}∷{}∷∷∷{}∷∷∷{}∷{}∷∷{}∷{}∷∷{}∷∷{}∷{}∷∷∷{}'.format(*selected))


def main(selected):
	mapa = open('mm.txt','r')
	cursor.hide()
	print(str(mapa.read()).format(*selected))
	input()
	cursor.show()


if __name__ == '__main__':
	main(selected)

