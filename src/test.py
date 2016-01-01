from simplevc.simplevc import mult, add, allPositions, tuple_add, tuple_mult,\
    allZeroCentrePositions, padPositions, randomHalfOf, padCentre
import unittest


class TestStringMethods(unittest.TestCase):
    def test_mult(self):
        self.assertEqual((2,4,6,8), mult((1,2,3,4),2))
        
    def test_tuple_mult(self):
        self.assertEqual((3,8), tuple_mult((1,2),(3,4)))
    
    def test_add(self):
        self.assertEqual((3,4,5,6), add((1,2,3,4),2))
    
    def test_allPositions_empty(self):
        self.assertEqual([], list(allPositions((0,0))))
        
    def test_allPositions_squares(self):
        self.assertEqual([(0,0)], list(allPositions((1,1))))
        self.assertEqual([(0,0),(0,1),(1,0),(1,1)], list(allPositions((2,2))))
        self.assertEqual([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], list(allPositions((3,3))))
    
    def test_allPositions_rects(self):
        self.assertEqual([(0,0),(0,1)], list(allPositions((1,2))))
        self.assertEqual([(0,0),(1,0)], list(allPositions((2,1))))
    
    def test_tuple_add(self):
        self.assertEqual((4,6), tuple_add((1,2),(3,4)))
        
    def test_allZeroCentrePositions_square(self):
        self.assertEqual([(0,0)],list(allZeroCentrePositions((1,1))))
        self.assertEqual([(-1,-1),(-1,0),(0,-1),(0,0)],list(allZeroCentrePositions((2,2))))
        self.assertEqual([(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)],list(allZeroCentrePositions((3,3))))
        
    def test_allZeroCentrePositions_rect(self):
        self.assertEqual([(0,-1),(0,0)],list(allZeroCentrePositions((1,2))))
        self.assertEqual([(-1,0),(0,0)],list(allZeroCentrePositions((2,1))))
    
    def test_padPositions(self):
        self.assertEqual([(4,7),(4,8),(5,7),(5,8)],list(padPositions((5,8),(2,2))))
        self.assertEqual([(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9)],list(padPositions((5,8),(3,3))))
        
    def test_padCentre(self):
        self.assertEqual((0,0),padCentre((0,0),(1,1)))
        self.assertEqual((1,1),padCentre((0,0),(2,2)))
        self.assertEqual((1,1),padCentre((0,0),(3,3)))
        self.assertEqual((2,2),padCentre((0,0),(4,4)))
        self.assertEqual((1,1),padCentre((1,1),(1,1)))
        self.assertEqual((3,3),padCentre((1,1),(2,2)))
        self.assertEqual((4,4),padCentre((1,1),(3,3)))
        self.assertEqual((6,6),padCentre((1,1),(4,4)))
    
    def test_randomHalfOf(self):
        self.assertEqual(5, len(randomHalfOf([0,1,2,3,4,5,6,7,8,9])))
        self.assertEqual(4, len(randomHalfOf([0,1,2,3,4,5,6,7,8])))

if __name__ == '__main__':
    unittest.main()