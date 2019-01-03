import unittest
import sys
sys.path.append('../Parts-Picker')
import api

class ApiTesting(unittest.TestCase):
	def testStoreDetails(self):
		self.assertEqual(api.getStoreDetails()['name'],'MX5 Shop')

if __name__ == '__main__':
	unittest.main()
