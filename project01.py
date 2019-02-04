import pygame
import sys
import random
import time
import os


# основной класс
class Game:
    def __init__(self):
        # ширина и высота окна
        self.width = 650
        self.height = 400

        # цвета, используемые в игре
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        self.fps = pygame.time.Clock()

        self.score = 0  # переменная, отвечающая за счет игры

    def errors(self):  # проверка наличия ошибок
        errors = pygame.init()

        if errors[1] > 0:
            sys.exit()

        else:
            print('OK')

    def surface(self):
        self.surface = pygame.display.set_mode((
            self.width, self.height))
        pygame.display.set_caption('Змейка')

    # принимаем все события, переданные игроком
    def event(self, changes):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changes = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    changes = "LEFT"
                elif event.key == pygame.K_UP:
                    changes = "UP"
                elif event.key == pygame.K_DOWN:
                    changes = "DOWN"

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.head = [100, 50]
                self.snake_body = [[100, 50], [90, 50], [80, 50]]
                self.snake_color = pygame.Color(0, 255, 0)
                self.direction = "RIGHT"
                self.changes = self.direction

        return changes

    def screen(self):
        pygame.display.flip()
        game.fps.tick(20)

    # функция, отвечающая за отображения счета игры
    def show_score(self, choice=1):

        s_font = pygame.font.SysFont('monaco', 30)
        s_surf = s_font.render(
            '    {0}'.format(self.score), True, self.red)
        s_rect = s_surf.get_rect()

        if choice == 1:
            s_rect.midtop = (100, 30)

        else:
            s_rect.midtop = (310, 250)

        self.surface.blit(s_surf, s_rect)

    # выводит на экран сообщение об окончании игры и счет
    def game_over(self):

        fullname = os.path.join('data', 'Game.png')
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:')
            raise SystemExit(message)

        image = pygame.transform.scale(image, (650, 400))
        newSurf = pygame.Surface((650, 400))
        newSurf.fill((255, 255, 0))
        newSurf.blit(image, (0, 0))
        game.surface.blit(newSurf, (0, 0))
        snake.changes = game.event(snake.changes)

        self.show_score(0)
        pygame.display.update()
        time.sleep(5)


# класс, отвечающий за отрисовку змейки
class Snake:
    def __init__(self, snake_color):
        self.head = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color

        self.direction = "RIGHT"
        self.changes = self.direction

    def direction_and_change(self):  #
        if self.changes == "RIGHT" and not self.direction == "LEFT":
            self.direction = self.changes

        elif self.changes == "LEFT" and not self.direction == "RIGHT":
            self.direction = self.changes

        elif self.changes == "UP" and not self.direction == "DOWN":
            self.direction = self.changes

        elif self.changes == "DOWN" and not self.direction == "UP":
            self.direction = self.changes

    def head1(self):
        if self.direction == "RIGHT":
            self.head[0] += 10

        elif self.direction == "LEFT":
            self.head[0] -= 10

        elif self.direction == "UP":
            self.head[1] -= 10

        elif self.direction == "DOWN":
            self.head[1] += 10

    def body(self, score, food_pos, screen_width, screen_height):
        self.snake_body.insert(0, list(self.head))

        if self.head[0] == food_pos[0] and self.head[1] == food_pos[1]:
            food_pos = [random.randrange(1, screen_width / 10) * 10, random.randrange(1, screen_height / 10) * 10]

            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):  # отрисовываем змейку
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    def boundaries(self, game_over, screen_width, screen_height):
        if any((
                self.head[0] > screen_width - 10 or self.head[0] < 0,
                self.head[1] > screen_height - 10 or self.head[1] < 0)):
            game_over()

        for block in self.snake_body[1:]:
            if block[0] == self.head[0] and block[1] == self.head[1]:
                game_over()


# Класс, отвечающий за отрисовку еды
class Stuff:
    def __init__(self, food_color, screen_width, screen_height):
        self.food_color = food_color
        self.x = 10
        self.y = 10

        self.food_pos = [random.randrange(1, screen_width / 10) * 10, random.randrange(1, screen_height / 10) * 10]

    def draw_food(self, play_surface):
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.x, self.y))


game = Game()
snake = Snake(game.green)
food = Stuff(game.red, game.width, game.height)

game.errors()
game.surface()
running = True

# основной игровой цикл
while running:
    fullname = os.path.join('data', 'snake.jpg')  # изображение, счет
    try:
        image = pygame.image.load(fullname)

    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = pygame.transform.scale(image, (100, 70))
    newSurf = pygame.Surface((100, 70))
    newSurf.fill((255, 255, 0))
    newSurf.blit(image, (0, 0))

    game.surface.blit(newSurf, (0, 0))
    snake.changes = game.event(snake.changes)
    pygame.display.flip()

    snake.direction_and_change()
    snake.head1()
    game.score, food.food_pos = snake.body(
        game.score, food.food_pos, game.width, game.height)
    snake.draw_snake(game.surface, game.white)
    fullname = os.path.join('data', 'snake.jpg')

    try:
        image = pygame.image.load(fullname)

    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = pygame.transform.scale(image, (100, 70))
    newSurf = pygame.Surface((100, 70))
    newSurf.fill((255, 255, 0))
    newSurf.blit(image, (0, 0))
    game.surface.blit(newSurf, (0, 0))
    snake.changes = game.event(snake.changes)
    pygame.display.flip()

    food.draw_food(game.surface)
    snake.boundaries(game.game_over, game.width, game.height)
    game.show_score()
    game.screen()

    fullname = os.path.join('data', 'snake.jpg')

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = pygame.transform.scale(image, (100, 70))
    newSurf = pygame.Surface((100, 70))
    newSurf.fill((255, 255, 0))
    newSurf.blit(image, (0, 0))
    game.surface.blit(newSurf, (0, 0))
    snake.changes = game.event(snake.changes)
    pygame.display.flip()
    snake.boundaries(game.game_over, game.width, game.height)
