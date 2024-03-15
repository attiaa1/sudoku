import pygame

# constants 
window_size = 900
grid_size = 9 
cell_size = window_size // grid_size


def main() -> None:
    
    pygame.init

    # display settings
    window = pygame.display.set_mode((window_size,window_size))
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load("imgs/rubiks_cube.png")
    pygame.display.set_icon(icon)
    

    # main loop
    running = True
    while running:
        for event in pygame.event.get():  # Get events from the queue
            if event.type == pygame.QUIT:
                running = False
        
        # White out the entire pygame display
        window.fill((255,255,255))
        
         # Draw the grid
        for i in range(grid_size + 1):
            pygame.draw.line(window, (0, 0, 0), (i * cell_size, 0), (i * cell_size, window_size))  # Vertical lines
            pygame.draw.line(window, (0, 0, 0), (0, i * cell_size), (window_size, i * cell_size))  # Horizontal lines
                
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()