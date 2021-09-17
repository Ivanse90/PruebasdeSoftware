def cells_state(cells,days):
    
    """
    This function gets  two arguments a list of cells with there statuses and the
    the second argument is the number of days
    it returns a list with the status after N days 
    """
 
    copyCell = cells.copy()

    for j in range(days):  
        anslist = []
        copyCell.insert(0,0)
        copyCell.insert(9,0)
        for i in range(len(copyCell)-2):
            if i == 0:
                if copyCell[0] == copyCell[2]:
                    anslist.insert(1,0)
                else:
                    anslist.insert(1,1)
            else:
                if copyCell[i] == copyCell[i+2]:
                    anslist.insert((i+1),0)
                else:
                    anslist.insert((i+1),1)
        copyCell = []
        copyCell = anslist            
    return anslist

# print(cells_state([0,1,1,0,1,0,1],1)) #[1, 1, 1, 0, 0, 0, 0]
# print(cells_state([0,1,1,0,1,0,1],2)) #[1, 0, 1, 1, 0, 0, 0]
# print(cells_state([0,1,1,0,1,0,1],5)) #[1, 1, 1, 0, 1, 1, 1]
# print(cells_state([0,1,1,0,1,0,1,1,0,1],3)) #[1, 1, 1, 0, 0, 0, 0]
# print(cells_state([0,1,1,0,1,0,1],0)) #[0, 1, 1, 0, 1, 0, 1]
# print(cells_state([0,1,1,0,2,0,1],1)) #[1, 1, 1, 0, 0, 0, 0]
# print(cells_state([],1)) #[]
# print(cells_state([0,1,1,0,-1,0,1],1)) #[1, 1, 1, 0, 0, 0, 0]
# print(cells_state([0,0,0,0,0,0,0],1)) #[0, 0, 0, 0, 0, 0, 0]
# print(cells_state([1,1,1,1,1,1,1],3)) #[1, 0, 1, 0, 1, 0, 1]
#######################