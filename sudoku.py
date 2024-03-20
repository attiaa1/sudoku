import pygame
import sys

# constants 
window_size = 900
grid_size = 9 
cell_size = window_size // grid_size

def main() -> None:
    
    # main game running loop
    running = True
    print("Running...")
    
    while running:
        for event in pygame.event.get():  # Get events from the queue
            if event.type == pygame.QUIT:
                running = False
                sys.exit("Shutting down...")
         
        init_grid()

        # Update the display     
        #pygame.display.update()

    pygame.quit()

def menu() -> str:
    BUTTON_WIDTH, BUTTON_HEIGHT = 200, 130
    WIDTH = HEIGHT = window_size
    
    # buttons for each difficulty
    button1 = pygame.Rect(WIDTH // 4 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    button2 = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    button3 = pygame.Rect(3 * WIDTH // 4 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), button1)
    pygame.draw.rect(window, (0, 255, 0), button2)
    pygame.draw.rect(window, (0, 0, 255), button3)

    font = pygame.font.Font(None,24)
    # Draw the text on the buttons
    text1 = font.render('Easy', True, (255,255,255))
    text2 = font.render('Medium', True, (255,255,255))
    text3 = font.render('Hard', True, (255,255,255))

    font = pygame.font.Font(None,48)
    text_title = font.render('Sudoku by Adam', True, (255,255,255))
    text_msg = font.render('Choose your difficulty below:', True, (255,255,255))

    window.blit(text_title, ((text_title.get_width() // 2), window_size // 9))
    window.blit(text_msg, ((text_title.get_width() // 2), window_size // 6))
    
    window.blit(text1, (button1.x + button1.width // 2 - text1.get_width() // 2, button1.y + button1.height // 2 - text1.get_height() // 2))
    window.blit(text2, (button2.x + button2.width // 2 - text2.get_width() // 2, button2.y + button2.height // 2 - text2.get_height() // 2))
    window.blit(text3, (button3.x + button3.width // 2 - text3.get_width() // 2, button3.y + button3.height // 2 - text3.get_height() // 2))

    pygame.display.update()
    
    difficulty = None
    while difficulty is None:
        # checking events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    difficulty = "easy"
                    break
                if button2.collidepoint(event.pos):
                    difficulty = "medium"
                    break
                if button3.collidepoint(event.pos):
                    difficulty = "hard"
                    break

            if event.type == pygame.QUIT:
                sys.exit("Shutting Down")

    pygame.display.update()
    
    print(f"Chosen difficulty is: {difficulty}")
    return difficulty

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
           
def user_input(default_grid) -> None:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            selected_row = mouse_y // cell_size
            selected_col = mouse_x // cell_size


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            try:  
                num = int(event.unicode)
                if not 1 <= num <= 9:
                    raise ValueError("Please enter a number between 1 and 9")
                default_grid[selected_row][selected_col] = num  

            except Exception as e:
                print(repr(e)) 
    
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
    
    pygame.init()
    pygame.font.init()

    # display settings
    window = pygame.display.set_mode((window_size,window_size))
    window.fill((0, 0, 0))
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load("imgs/rubiks_cube.png")
    pygame.display.set_icon(icon)
    pygame.display.flip()

    difficulty = menu()
    main()