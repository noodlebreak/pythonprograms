#!/usr/bin/python
"""tests function seven_seg provided by module seven_seg"""
import unittest
import ssc as seven_seg
from test_vectors import test_vectors

class MyTest(unittest.TestCase):
	def test_all(self):
		try:
			for i in range(10):
				x = str(i)
				self.assertEqual(seven_seg.seven_seg(x), test_vectors[x])
	
			for i in test_vectors:
				x = i
				self.assertEqual(seven_seg.seven_seg(i), test_vectors[i])

		except AssertionError:
			print "\n'" + x + "'", 'should result in:'
			print test_vectors[x]
			print 'but your module produced:'
			print seven_seg.seven_seg(x)
			raise

if __name__ == '__main__':
	unittest.main()

