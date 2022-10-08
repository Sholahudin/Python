from operator import length_hint
import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen) -> None:
        self.image = pygame.image.load('resources/apple.jpeg').convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE


class Snake:
    def __init__(self, parent_screen, length) -> None:
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('resources/block.jpeg').convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "down"

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = "left"
    
    def move_right(self):
        self.direction = "right"
    
    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SIZE
            self.draw()
        if self.direction == "down":
            self.y[0] += SIZE
            self.draw()
        if self.direction == "left":
            self.x[0] -= SIZE
            self.draw()
        if self.direction == "right":
            self.x[0] += SIZE
            self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()


class Game:
    def __init__(self): 
        pygame.init()
        pygame.display.set_caption("Game Ular NOKIA")
        self.x_body = 1000
        self.y_body = 800
        self.surface = pygame.display.set_mode((self.x_body,self.y_body))

        pygame.mixer.init()
        self.play_background_music()
        self.surface.fill((121, 237, 127))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
    
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def is_gone(self, x1, y1, x2, y2):
        if x1 < 0 or x1 > x2:
            return True
        if y1 < 0 or y1 > y2:
            return True
        return False

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpeg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #snake menabrak apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        if self.is_gone(self.snake.x[0], self.snake.y[0], self.x_body, self.y_body):
                self.play_sound("crash")
                raise "Game over"

        #snake menabrak tubuhnya
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game over"
            

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255,255,255))
        self.surface.blit(score,(800,10))

    def show_pause(self):
        font = pygame.font.SysFont('arial', 30)
        pause = font.render("Game Paused. Press Enter to Continue ...", True, (255, 255, 255))
        self.surface.blit(pause,(250,400))
        pygame.display.flip()

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is: {self.snake.length}", True, (255,255,255))
        self.surface.blit(line1,(200,300))
        line2 = font.render(f"To play again please Enter. To exit press Escape.", True, (255,255,255))
        self.surface.blit(line2,(200,350))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def timer(self):
        achieve = self.snake.length
        if achieve <= 5:
            time.sleep(0.3)
        elif achieve <= 10:
            time.sleep(0.25)
        elif achieve <= 15:
            time.sleep(0.2)
        elif achieve <= 20:
            time.sleep(0.15)
        elif achieve <= 25:
            time.sleep(0.1)
        else:
            time.sleep(0.05)

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_SPACE:
                        self.show_pause()
                        pause = True

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_UP and self.snake.direction != "down":
                            self.snake.move_up()
                        if event.key == K_DOWN and self.snake.direction != "up":
                            self.snake.move_down()
                        if event.key == K_LEFT and self.snake.direction != "right":
                            self.snake.move_left()
                        if event.key == K_RIGHT and self.snake.direction !="left":
                            self.snake.move_right()
                    
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            self.timer()

if __name__ == "__main__":
    game = Game()
    game.run()