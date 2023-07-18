#Code has progressed by psuedo-coding but still counts the amount of prisoners freed from a line of cells.
#In a game loop, the player inputs what cell they want to try. If this cell is unlocked, a prisoner is freed
#and added to the count. That cell and those to the left are removed from the game.
#The remaining cells locked and unlocked values are reversed by switching from 0 to 1 or vice versa.
#The game ends when there are no cells left to try and a count of prisoners freed is returned.

freed_count = 0
cell_list = [1,1,1,0,0,1,0]
while(1):
	#Makes sure the array index is not exceeded by ending the game when there are no more cells.
    if len(cell_list) <= 0:
	    break
    else:
        print("You are staring at a line of cells. If the cell is labelled with a '1' the cell is unlocked. If the label is '0' the cell is locked. You can choose any of the cells to try to free a prisoner from. Once you've tried that cell, you can't try it again, and you can't try any of the cells to its left. You will only be able to try the cells to its right. Additionally; any cell that was locked will unlock. Any cell which was unlocked will lock.")
        print("So far, the amount of prisoners you have freed is", freed_count)
        print("These are the cells you can now choose from:\n ", cell_list)
        cell_num = int(input("Please input the number of the cell you want to open: "))-1
                          
        #ends game if a number above cells left or no cells are left.                  
        if len(cell_list) <= 0 or cell_num > len(cell_list):
        	 break
        elif cell_list[cell_num] == 1:
           freed_count += 1
           print("You have freed a prisoner!")

			#Flips the locked and unlocked status of the cells
           for cell_counter in range(0, len(cell_list)):
              if cell_list[cell_counter] == 1:
                  cell_list[cell_counter] = 0
              else:
                  cell_list[cell_counter] = 1
              if len(cell_list) <= 0:
                  break
        else:
            print("That cell is locked!")
                                    
            # Flips the locked and unlocked status of the cells                       
            for cell_counter in range(0, len(cell_list)):
              if cell_list[cell_counter] == 1:
                  cell_list[cell_counter] = 0
              else:
                  cell_list[cell_counter] = 1
         
        #deletes all cells from cell tried to the left
        #The second line is, admitedly, a bit of a hack in that I can't get the delete to remove the 0 index. 
        #I have then added a line to do so.                             
        del cell_list[cell_num:0:-1]
        cell_list.pop(0)
        if len(cell_list) <= 0:
            break 
    if len(cell_list) <= 0:
      break
print("It's the end of the game! The amount of prisoners you have freed is", freed_count)

freed_count = 0
cell_list = [1,1,1,1,1,1,1]

while(1):
    cell_counter_zeroed = len(cell_list)
    if cell_counter_zeroed == 0:
      break
    elif len(cell_list) <= 0:
	    break
    else:
        print("You are staring at a line of cells. If the cell is labelled with a '1' the cell is unlocked. If the label is '0' the cell is locked. You can choose any of the cells to try to free a prisoner from. Once you've tried that cell, you can't try it again, and you can't try any of the cells to its left. You will only be able to try the cells to its right. Additionally; any cell that was locked will unlock. Any cell which was unlocked will lock.")
        print("So far, the amount of prisoners you have freed is", freed_count)
        print("These are the cells you can now choose from:\n ", cell_list)
        cell_num = int(input("Please input the number of the cell you want to open: "))-1
        if len(cell_list) <= 0 or cell_num > len(cell_list):
        	 break
        elif cell_list[cell_num] == 1:
           freed_count += 1
           print("You have freed a prisoner!")
           for cell_counter in range(0, len(cell_list)):
              if cell_list[cell_counter] == 1:
                  cell_list[cell_counter] = 0
              elif cell_list[cell_counter] == 0:
                  cell_list[cell_counter] = 1
              elif len(cell_list) <= 0:
                  break
        else:
            cell_counter_zeroed = len(cell_list)
            for cell_counter in range(0, len(cell_list)):
                cell_counter_zeroed = cell_counter_zeroed - (1 - (cell_list[cell_counter]))
            if cell_counter_zeroed == 0:
              print("All the cells are locked. You can't free anyone else!")
              break
            print("That cell is locked! You can't free that prisoner. Try again.")
            continue
        del cell_list[cell_num:0:-1]
        cell_list.pop(0)
        if len(cell_list) <= 0:
            break 
    if len(cell_list) <= 0:
      break
print("It's the end of the game! The amount of prisoners you have freed is", freed_count)


