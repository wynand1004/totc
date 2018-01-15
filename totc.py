# Tale of Two Cities by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL

# Import SPGL
import spgl
import math

# Create Classes
class Totc(spgl.Game):
    def __init__(self, screen_width, screen_height, background_color, title, splash_time):
        spgl.Game.__init__(self, screen_width, screen_height, background_color, title, splash_time)

        self.grid = []
        for grid_y in range(0, 30):
            self.grid.append([])
        
        # Set up default power blocks
        for grid_y in range(0, 10):
            for grid_x in range(0, 40):
                screen_x, screen_y = self.convert_grid_xy_to_screen_xy(grid_x, grid_y)
                self.grid[grid_y].append(Powerblock("square", "black", screen_x, screen_y))                
                self.grid[grid_y][grid_x].shapesize(0.9, 0.9, None)
                self.grid[grid_y][grid_x].setheading(90)

        for grid_y in range(20, 30):
            for grid_x in range(0, 40):
                screen_x, screen_y = self.convert_grid_xy_to_screen_xy(grid_x, grid_y)
                self.grid[grid_y].append(Powerblock("square", "black", screen_x, screen_y))                
                self.grid[grid_y][grid_x].shapesize(0.9, 0.9, None)
                self.grid[grid_y][grid_x].setheading(90)


        # Draw green city foundation
        for grid_x in range(0, 40):
            self.grid[0][grid_x].color("green")

        # Draw red city foundation
        for grid_x in range(0, 40):
            self.grid[29][grid_x].color("red")

    def click(self, screen_x, screen_y):
        grid_x, grid_y = self.convert_screen_xy_to_grid_xy(screen_x, screen_y)

        # Check to see if it is already an active powerblock
        if self.grid[grid_y][grid_x].color()[0] == "red":
            self.grid[grid_y][grid_x].change_type()
        
        # Check to make sure block below is red 
        elif self.grid[grid_y+1][grid_x].color()[0] == "red" and (grid_y > 19 and grid_y < 29):    
            self.grid[grid_y][grid_x].color("red")

    def convert_screen_xy_to_grid_xy(self,screen_x,screen_y):
        grid_x = math.floor((screen_x + 400) / 20)
        grid_y = math.floor((screen_y - 300) / -20)
        return (grid_x, grid_y)

    def convert_grid_xy_to_screen_xy(self, grid_x, grid_y):
            screen_x = -390 + (20 * grid_x)
            screen_y = 290 - (20 * grid_y)
            return (screen_x, screen_y)

class Powerblock(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.power = 100
        self.type = "power"

    def change_type(self):
        if self.type == "power":
            self.type = "shield"
        elif self.type == "shield":
            self.type = "weapon"
        elif self.type == "weapon":
            self.type = "power"

        self.change_shape()

    def change_shape(self):
        if self.type == "power":
            self.shape("square")
        elif self.type == "shield":
            self.shape("circle")
        elif self.type == "weapon":
            self.shape("triangle")

# Create Functions

# Initial Game setup
game = Totc(800, 600, "white", "Tale of Two Cities /u/wynand1004 AKA @TokyoEdTech", 0)

# Create Sprites

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()

    # Do calculations

