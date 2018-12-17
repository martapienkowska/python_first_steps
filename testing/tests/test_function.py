import unittest

from fun import function
from fun.function import fun1
#aby katalogi były pakietami w obu dodaję puste pliki __init__.py
#aby odpalić wszystkie funkcje z katalogu używam funkcji python3 -m unittest discover (w katalogu testing)
#aby odpalić tylko ten test używam python3 -m unittest tests.test_function
#aby odpalić jeden test z test function używam python3 -m unittest tests.test_function.PrimesTestCase.test_fun1
#jeśli mam zainstaloway nose2 (sudo pip install nose2) mogę odpalić w katalogu python3 nose2




class PrimesTestCase(unittest.TestCase):
	def test_fun1(self):
#WSZYSTKIE METODY MUSZĄ ZACZYNAĆ SIĘ OD TEST_!!!
		self.assertEqual(fun1(), 75)

if __name__ == '__main__':
	unittest.main()
