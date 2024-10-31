import pygame
import random
import math

GRID_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
OBSTACLE_DENSITY = 0.2

def create_grid():
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if random.random() < OBSTACLE_DENSITY:
                grid[x][y] = 1  # 1 represents an obstacle
    return grid

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = (0, 1)  # initial direction (down)

    def move(self, grid):
        next_x = self.x + self.direction[0]
        next_y = self.y + self.direction[1]
        
        # Detect obstacle
        if grid[next_x][next_y] == 1:
            self.avoid_obstacle()
        else:
            self.x, self.y = next_x, next_y  # Move to the next cell

    def avoid_obstacle(self):
        # Rotate right if obstacle is detected
        if self.direction == (0, 1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, 1)

def draw_grid(screen, grid, robot):
    screen.fill((255, 255, 255))
    cell_size = SCREEN_WIDTH // GRID_SIZE
    
    # Draw grid and obstacles
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect)
            else:
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    # Draw robot
    robot_rect = pygame.Rect(robot.x * cell_size, robot.y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (0, 255, 0), robot_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    grid = create_grid()
    robot = Robot(0, 0)  # Starting position

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        robot.move(grid)
        draw_grid(screen, grid, robot)
        pygame.display.flip()
        clock.tick(5)  # Adjust speed

    pygame.quit()

if __name__ == "__main__":
    main()
