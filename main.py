from print_grid import grid

arr = [[0,0,0],[0,0,0],[0,0,0]]
grid = grid(arr)
grid.print_grid()

for i in range(9):
    row = int(input("Enter the row name: "))
    col = int(input("Enter the column name: "))
    if(arr[row][col] == 0):
        if(i%2):
            arr[row][col] = 1
        else:
            arr[row][col] = 2
    else:
        print("\nThat square has already been marked! Please select another square")
        i = i-1
        continue
    grid.print_grid()
    res = grid.grid_checker()
    if (res == 1):
        print("\nPlayer 1 wins the game!")
        break
    elif(res == 2):
        print("\nPlayer 2 wins the game!")
        break
    elif(i == 8):
        print("\nThe game has ended in a draw!")
        