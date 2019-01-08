import unittest
import sys
sys.path.append('../Parts-Picker')
import api
import dialogs
import utils
from PyQt4 import QtGui
from PyQt4.QtCore import *
class ApiTesting(unittest.TestCase):
	def testStoreDetails(self):
		self.assertEqual(api.getStoreDetails()['name'],'MX5 Shop')

	def testArticleCount(self):
		self.assertTrue(api.getArtikelCount()>100)
		self.assertEqual(len(api.getArtikels()),api.getArtikelCount())

class WindowTesting(unittest.TestCase)
	def testWindowVolgorde(self):
		#start factuur.py
		#Click next 3 times
		#-check window name

	def testProductGrid(self):
		#dunno

	def testOrderlijst(self):
		#klik een paar dingen
		#klopt de lijst? inhoud/display?

class LatexTesting(unittest.TestCase)
	def testAutoFactuur(self):
		#data['Auto']

class dialogTesting(unittest.TestCase):
	def testUrenDialog(self):
		widget = dialogs.UrenDialog()
		widget.editUren.setValue(1.5)
		widget.editOmschrijving.setText("Test Uren")
		widget.done(1)
		retValue = widget.return_strings()
		self.assertEqual(retValue,[1.5, "Test Uren"])
		urenItem = utils.UrenItem(retValue[0],retValue[1])
		self.assertEqual(urenItem.totaalPrijs(),1.5*65.00)

	def testVrijveldDialog(self):
		widget = dialogs.VrijVeldDialog()
		widget.editAantal.setValue(3)
		widget.editPrijs.setValue(5.5)
		widget.editNaam.setText("Test naam")
		widget.tax21.click()
		widget.done(1)
		retvalue = widget.return_strings()
		orderItem = utils.OrderItem(retvalue[0],retvalue[1],retvalue[2],retvalue[3])
		self.assertEqual(orderItem.totaalPrijs(),5.5*3)
		self.assertEqual(orderItem.Tax,21)

	def testSearchDialog(self):
		widget = dialogs.SearchDialog()
		widget.editZoekNaar.setText("ZoekTekst")
		widget.zoekAlles.click()
		retvalue = widget.return_strings()
		self.assertEqual(retvalue,["ZoekTekst",False])

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	unittest.main(verbosity=2)
