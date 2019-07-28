from bs4 import BeautifulSoup
import sys

target = open(sys.argv[1], 'r')
bs = BeautifulSoup(target, 'lxml')
target.close()

print(bs.select('span'))
