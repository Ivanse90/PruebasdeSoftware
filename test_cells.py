from cell_simulate import cells_state
from random import choice


def test_fuction_cell(cells_number):
    """
    This function gets two parameters cells_number which is the array lenght of cells
    and days that is the numer of days to simulate the state of cells
    and it will return an array 0 and 1 with the state of cell after "days"
    """
    cells =[0,1]
    cells_array =[]
    for i in range(cells_number):
        cells_array.append(choice(cells))
    
    sequence = [i for i in range(cells_number)]
    
    number = choice(sequence)  
    print("After ",number,"days, the state of cells", cells_array, "is :")
    return cells_state(cells_array,number)


print(test_fuction_cell(7))

