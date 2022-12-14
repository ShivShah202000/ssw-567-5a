"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle1 import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')
    #RightAngle Triangle
        self.assertEqual(classifyTriangle(5,3,4),'Right')
    #testEquilateralTriangles
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral')
        self.assertEqual(classifyTriangle(3,3,4), 'Isoceles')
    #testScalene
    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 5, 7),'Scalene')
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(2,2,3), "Isoceles")
    def testTriangle(self):
        self.assertEqual(classifyTriangle(1.1,2,3),'Scalene')
        self.assertEqual(classifyTriangle(3,5,1),'Scalene')
    def testTriangle1(self):
        self.assertEqual(classifyTriangle(-5,3,5),'InvalidInput')
        self.assertEqual(classifyTriangle(230,3,5),'InvalidInput')
        #self.assertEqual(classifyTriangle(12,3,18),'NotATriangle')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

