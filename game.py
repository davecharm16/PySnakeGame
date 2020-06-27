import pygame
class Snake:
    def __init__(self, X, Y, image):
        self.snakeHead = pygame.image.load(image)
        self.X = X
        self.Y = Y
    def move(self):
        pygame.display.blit(self.snakeHead, (self.X, self.Y))
    
class Game:
    running = True
    def __init__(self):
        # self.bg_image = pygame.image.load(bg)
        self.size = (632,632)
    def run(self):
        screen = pygame.display.set_mode(self.size)
        pygame.init()
        while Game.running:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event == pygame.event.QUIT:
                    Game.running = False



game1 = Game()
game1.run()
