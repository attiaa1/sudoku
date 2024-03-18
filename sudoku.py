import pygame

# constants 
window_size = 450
grid_size = 9 
cell_size = window_size // grid_size


pygame.init()
pygame.font.init()

# display settings
window = pygame.display.set_mode((window_size,window_size))
pygame.display.set_caption("Sudoku")
icon = pygame.image.load("imgs/rubiks_cube.png")
pygame.display.set_icon(icon)

init_grid = False

def main() -> None:
    
    # main game running loop
    running = True
    print("Running...")
    
    while running:
        for event in pygame.event.get():  # Get events from the queue
            if event.type == pygame.QUIT:
                running = False
        
        init_grid()
        


        # Update the display     
        #pygame.display.update()

    pygame.quit()
    
def generate_grid():
    grid = [
        [1,2,3,4,5,6,7,8,9],
        [2,2,3,4,5,6,7,8,9],
        [3,2,3,4,5,6,7,8,9],
        [4,2,3,4,5,6,7,8,9],
        [5,2,3,4,5,6,7,8,9],
        [6,2,3,4,5,6,7,8,9],
        [7,2,3,4,5,6,7,8,9],
        [8,2,3,4,5,6,7,8,9],
        [9,2,3,4,5,6,7,8,9]
    ]
    return grid

def solve_grid() -> None:
    pass

def remove_grid() -> None:
    pass
    
def draw_board(grid) -> None:
    
    # nested for loop which will call draw_cell
    for i in range(9):
        for j in range(9):
           num = grid[i][j]
           if num != 0:
               draw_cell(i,j,num)
    
    pygame.display.update()
           
    
    
def draw_cell(row, column, num) -> None:
    font = pygame.font.Font(None,int(cell_size/2))
    text = font.render(str(num), True, (0,0,0))
    window.blit(text, (column * cell_size + cell_size // 4, row * cell_size + cell_size // 4))

def isValidSudoku(grid) -> bool:
    seen = set()
    for i in range(9):
        for j in range(9):
            number = grid[i][j]  
            if number != "0":
                # Create unique identifiers for row, column, and sub-box
                row = str(number) + "row" + str(i)
                column = str(number) + "column" + str(j)
                block = str(number) + "block" + str(i // 3) + "/" + str(j // 3)

                # Check if any of these identifiers already exist in the set
                if row in seen or column in seen or block in seen:
                    return False

                # Add the identifiers to the set
                seen.add(row)
                seen.add(column)
                seen.add(block)

    return True  

def init_grid() -> None:
    window.fill((255,255,255))
    # Draw the grid
    for i in range(grid_size):
        for j in range(grid_size):
            rect = pygame.Rect(i*cell_size, j*cell_size, cell_size, cell_size)
            pygame.draw.rect(window, (0, 0, 0), rect, 1)

    new_grid = generate_grid()
    draw_board(new_grid)
    


if __name__ == "__main__":
    main()