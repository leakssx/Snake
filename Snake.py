import pygame
import random

class Snake():
    """
    Snake is a Game
    """

    def __init__(self):
        self.yellow = (255, 255, 0)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.snake = [[300, 300],[300,320]]
        self.running = True
        self.food_pos = []
        self.direction = "Up"  
        self.move_allowed = True
        self.GameLoop()


    def GameLoop(self):
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                key_input = pygame.key.get_pressed()
                
                if key_input[pygame.K_UP] and self.direction != "Down" and self.move_allowed:
                    self.direction = "Up"
                    self.move_allowed = False
                elif key_input[pygame.K_DOWN] and self.direction != "Up" and self.move_allowed:
                    self.direction = "Down"
                    self.move_allowed = False
                elif key_input[pygame.K_RIGHT] and self.direction != "Left" and self.move_allowed:
                    self.direction = "Right"
                    self.move_allowed = False
                elif key_input[pygame.K_LEFT] and self.direction != "Right" and self.move_allowed:
                    self.direction = "Left"
                    self.move_allowed = False
                
            self.screen.fill((0,0,0))
            self.HeadPosition = self.snake[-1]
            self.MoveSnake()
            self.move_allowed = True
            self.MapBorder()
            self.DrawSnake()
            self.Food()
            self.GetTailHit()
            
            pygame.display.flip()
            self.clock.tick(13)
    def DrawSnake(self):
        for index, value in enumerate(self.snake):
            try:
                next_value =  self.snake[index + 1]
                if next_value[0] > value[0]:
                    pygame.draw.rect(self.screen, self.yellow, (value[0]- 8, value[1] -8, 20 ,16))
                elif next_value[0] < value[0]:
                    pygame.draw.rect(self.screen, self.yellow, (value[0]- 12, value[1] - 8, 20 ,16))
                elif next_value[1] > value[1]:
                    pygame.draw.rect(self.screen, self.yellow, (value[0]- 8, value[1] -8, 16 ,20))
                elif next_value[1] < value[1]:
                    pygame.draw.rect(self.screen, self.yellow, (value[0] - 8, value[1] - 12, 16 ,20))
            except:
                pygame.draw.rect(self.screen, self.blue, (value[0]- 8, value[1] -8, 16 ,16))
    def SnakeDead(self):
        self.snake = [[300,300],[320,300]]
    def MapBorder(self):
        border_start = 0
        border_end = 580
        border_thickness = 20

        pygame.draw.rect(self.screen, self.green, (border_start, border_start, border_end, border_thickness))
        pygame.draw.rect(self.screen, self.green, (border_start, border_start, border_thickness, border_end))
        pygame.draw.rect(self.screen, self.green, (border_end, border_start, border_thickness, border_end))
        pygame.draw.rect(self.screen, self.green, (border_start, border_end, border_end + border_thickness, border_thickness))
        
        if not border_end > self.HeadPosition[1] > border_thickness:
            self.SnakeDead()
        if not border_end > self.HeadPosition[0] > border_thickness:
            self.SnakeDead()  
    def MoveSnake(self):
                
        for index, value in enumerate(self.snake):
            try:
                self.snake[index] = [int(self.snake[index + 1][0]), int(self.snake[index + 1][1])]
            except:
                if self.direction == "Down":
                    self.snake[index][1] += 20
                if self.direction == "Up":
                    self.snake[index][1] -= 20
                if self.direction == "Left":
                    self.snake[index][0] -=20
                if self.direction == "Right":
                    self.snake[index][0] +=20
            
    def Food(self):
        
        while not self.food_pos:
            x = random.randint(2,28) * 20
            y = random.randint(2,28) * 20
            if not [x , y] in self.snake:
                self.food_pos = [x,y]
        pygame.draw.rect(self.screen, self.red, (self.food_pos[0] - 8, self.food_pos[1] -8, 16,16))   
        
        if self.HeadPosition == self.food_pos:
            self.food_pos = []
            self.snake.insert(0, self.snake[0])
    def GetTailHit(self):
        if self.HeadPosition in self.snake[:-1]:
            self.SnakeDead()
if __name__ == "__main__":
    Snake()