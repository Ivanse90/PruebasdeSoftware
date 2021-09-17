from cell_simulate import cells_state
from random import choice
import unittest


# def test_fuction_cell(cells_number):
#     """
#     This function gets two parameters cells_number which is the array lenght of cells
#     and days that is the numer of days to simulate the state of cells
#     and it will return an array 0 and 1 with the state of cell after "days"
#     """
#     cells =[0,1]
#     cells_array =[]
#     for i in range(cells_number):
#         cells_array.append(choice(cells))
    
#     sequence = [i for i in range(cells_number)]
    
#     number = choice(sequence)  
#     print("After ",number,"days, the state of cells", cells_array, "is :")
#     return cells_state(cells_array,number)


# print(test_fuction_cell(7))

class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(cells_state([0,1,1,0,1,0,1],1), [1, 1, 1, 0, 0, 0, 0])
    
    def test_two(self):
        self.assertEqual(cells_state([0,1,1,0,1,0,1],2), [1, 0, 1, 1, 0, 0, 0])

    def test_three(self):
        self.assertEqual(cells_state([0,1,1,0,1,0,1],5), [1, 1, 1, 0, 1, 1, 1])

    def test_four(self):
        self.assertEqual(cells_state([0,1,1,0,1,0,1,1,0,1],3), [0, 0, 1, 1, 0, 1, 0, 1, 1, 1])

    def test_five(self):
        self.assertEqual(cells_state([0,1,1,0,1,0,1],0), [0, 1, 1, 0, 1, 0, 1])
    
    def test_six(self):
        self.assertEqual(cells_state([0,1,1,0,2,0,1],1), [1, 1, 1, 0, 0, 0, 0])

    def test_seven(self):
        self.assertEqual(cells_state([0,1,1,0,-1,0,1],1), [1, 1, 1, 0, 0, 0, 0])
    
    def test_eigth(self):
        self.assertEqual(cells_state([0,0,0,0,0,0,0],1), [0, 0, 0, 0, 0, 0, 0])

    def test_nine(self):
        self.assertEqual(cells_state([1,1,1,1,1,1,1],3), [1, 0, 1, 0, 1, 0, 1])
    
    def test_eleven(self):
        self.assertEqual(cells_state([],1), [])



if __name__ == '__main__':
    unittest.main()


prueba_calidad = TestMethods()
 