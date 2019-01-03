import unittest
import sys
sys.path.append('../Parts-Picker')
import api

class ApiTesting(unittest.TestCase):
	def testStoreDetails(self):
		self.assertEqual(api.getStoreDetails()['name'],'MX5 Shop')

	def testArticleCount(self):
		self.assertTrue(api.getArtikelCount()>100)
		self.assertEqual(len(api.getArtikels()),api.getArtikelCount())


if __name__ == '__main__':
	unittest.main()
