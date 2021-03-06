import pygame
from pygame import *
import pygame_gui
import os
import sys
import random
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 832, 540
win_size = win_width, win_height = 830, 610
FPS = 8
WIDTH_2 = 820
HEIGHT_2 = 550
FPS_2 = 65
GRAVITY = 0.15
MAPS_DIR = 'maps'
TILE_SIZE = 32
ENEMY_EVENT_TYPE = 30
speed_easy = 1000
speed_medium = 800
speed_hard = 400
screen_rect = (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
all_sprites = pygame.sprite.Group()
entities = pygame.sprite.Group()
monsters = pygame.sprite.Group()
sp = []
level = [
    "------------------------------------------------------------------",
    "-                                                              * -",
    "-                                                                -",
    "-                               ---                              -",
    "----      ---           ----                  ----    ---        -",
    "-                                                             ----",
    "-                                *                               -",
    "-*             ----                   --                         -",
    "-                     ---                        *        -     --",
    "-                *                           ---                 -",
    "-     ----                   ----                            -   -",
    "-                                                                -",
    "-                                                                -",
    "-------------------------------------------+++++++++++++++++++----"]


#работа с картой лабиринта
class Labyrinth:
    def __init__(self, file_name, free_tiles, finish_tile, hero, num):
        self.f = pygame.font.SysFont('serif bold', 40)
        self.a = 0
        self.b = 0
        self.map = []
        self.count_num = 0
        self.hero = hero
        self.restart = load_image("restart.png")
        self.pause = load_image("pause.png")
        self.image = load_image("star.png", -1)
        self.home = load_image("home.png")
        if num == 1:
            self.rect_1 = self.image.get_rect(center=(592, 48))
            self.rect_2 = self.image.get_rect(center=(592, 336))
            self.rect_3 = self.image.get_rect(center=(112, 304))
        elif num == 2:
            self.rect_1 = self.image.get_rect(center=(240, 144))
            self.rect_2 = self.image.get_rect(center=(112, 304))
            self.rect_3 = self.image.get_rect(center=(720, 401))
            self.rect_4 = self.image.get_rect(center=(48, 48))
        elif num == 3:
            self.rect_1 = self.image.get_rect(center=(782, 48))
            self.rect_2 = self.image.get_rect(center=(464, 400))
            self.rect_3 = self.image.get_rect(center=(48, 400))
            self.rect_4 = self.image.get_rect(center=(176, 240))
            self.rect_5 = self.image.get_rect(center=(655, 208))
        with open(f"{MAPS_DIR}/{file_name}") as input_file:
            for line in input_file:
                self.map.append(list(map(int, line.split())))
            self.height = len(self.map)
            self.width = len(self.map[0])
            self.tile_size = TILE_SIZE
            self.free_tiles = free_tiles
            self.finish_tile = finish_tile

    def render(self, screen, num):
        colors = {0: (0, 0, 0), 1: (0, 0, 200), 2: (230, 230, 0)}
        screen.blit(self.restart, (13, 470))
        screen.blit(self.pause, (80, 470))
        screen.blit(self.home, (150, 470))
        for y in range(self.height):
            for x in range(self.width):
                rec = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                screen.fill(colors[self.get_tile_id((x, y))], rec)
                if num == 1:
                    self.b = 3
                    if self.count_num != 3:
                        rec = pygame.Rect(22 * self.tile_size,
                                           13 * self.tile_size,
                                           self.tile_size, self.tile_size)
                        screen.fill((0, 0, 200), rec)
                    if self.count_num == 0:
                        self.a = 0
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_2)
                        if self.get_position() == (18, 10):
                            self.count_num = 1
                    elif self.count_num == 1:
                        self.a = 1
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_3)
                        if self.get_position() == (3, 9):
                            self.count_num = 2
                    elif self.count_num == 2:
                        self.a = 2
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_1)
                        if self.get_position() == (18, 1):
                            self.count_num = 3
                    elif self.count_num == 3:
                        self.a = 3
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                elif num == 2:
                    self.b = 4
                    if self.count_num != 4:
                        rect = pygame.Rect(22 * self.tile_size,
                                           0 * self.tile_size,
                                           self.tile_size, self.tile_size)
                        screen.fill((0, 0, 200), rect)
                    if self.count_num == 0:
                        self.a = 0
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_1)
                        if self.get_position() == (7, 4):
                            self.count_num = 1
                    elif self.count_num == 1:
                        self.a = 1
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_3)
                        if self.get_position() == (22, 12):
                            self.count_num = 2
                    elif self.count_num == 2:
                        self.a = 2
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_2)
                        if self.get_position() == (3, 9):
                            self.count_num = 3
                    elif self.count_num == 3:
                        self.a = 3
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_4)
                        if self.get_position() == (1, 1):
                            self.count_num = 4
                    elif self.count_num == 4:
                        self.a = 4
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                elif num == 3:
                    self.b = 5
                    if self.count_num != 5:
                        rect = pygame.Rect(2 * self.tile_size,
                                           0 * self.tile_size,
                                           self.tile_size, self.tile_size)
                        screen.fill((0, 0, 200), rect)
                    if self.count_num == 0:
                        self.a = 0
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_2)
                        if self.get_position() == (14, 12):
                            self.count_num = 1
                    elif self.count_num == 1:
                        self.a = 1
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_3)
                        if self.get_position() == (1, 12):
                            self.count_num = 2
                    elif self.count_num == 2:
                        self.a = 2
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_1)
                        if self.get_position() == (24, 1):
                            self.count_num = 3
                    elif self.count_num == 3:
                        self.a = 3
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_4)
                        if self.get_position() == (5, 7):
                            self.count_num = 4
                    elif self.count_num == 4:
                        self.a = 4
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))
                        screen.blit(self.image, self.rect_5)
                        if self.get_position() == (20, 6):
                            self.count_num = 5
                    elif self.count_num == 5:
                        self.a = 5
                        text = f"СОБРАНО ЗВЁЗД {self.a}/{self.b}"
                        res = self.f.render(text, False, (255, 255, 255))
                        screen.blit(res, (500, 480))

    def get_position(self):
        position = self.hero.get_position()
        return position

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles

    def find_path_step(self, start, target, second=(0, 0)):
        INF = 1000
        x, y = start
        distance = [[INF] * self.width for _ in range(self.height)]
        distance[y][x] = 0
        prev = [[None] * self.width for _ in range(self.height)]
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < self.width and 0 < next_y < self.height and \
                        self.is_free((next_x, next_y)) and\
                        distance[next_y][next_x] == INF:
                    distance[next_y][next_x] = distance[y][x] + 1
                    prev[next_y][next_x] = (x, y)
                    queue.append((next_x, next_y))
        x, y = target
        if distance[y][x] == INF or start == target or start == second:
            return start
        while prev[y][x] != start:
            x, y = prev[y][x]
        return x, y


#работа с управляемым героем лабиринта
class Hero:
    def __init__(self, position):
        self.x, self.y = position

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        center = self.x * TILE_SIZE + TILE_SIZE // 2,\
                 self.y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, (255, 255, 255), center, TILE_SIZE // 2)


#враги в лабиринте
class Enemy:
    def __init__(self, position, num):
        self.x, self.y = position
        if num == 1:
            self.delay = speed_easy
        elif num == 2:
            self.delay = speed_medium
        else:
            self.delay = speed_hard
        pygame.time.set_timer(ENEMY_EVENT_TYPE, self.delay)

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        center = self.x * TILE_SIZE + TILE_SIZE // 2,\
                 self.y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, (255, 0, 0), center, TILE_SIZE // 2)


#лабиринт
class Game:
    def __init__(self, labyrinth, hero, enemy, num, enemy_2=0):
        self.labyrinth = labyrinth
        self.hero = hero
        self.enemy_1 = enemy
        self.enemy_2 = enemy_2
        self.num = num

    def render(self, screen):
        if self.num == 1:
            self.labyrinth.render(screen, 1)
            self.hero.render(screen)
            self.enemy_1.render(screen)
        elif self.num == 2:
            self.labyrinth.render(screen, 2)
            self.hero.render(screen)
            self.enemy_1.render(screen)
            self.enemy_2.render(screen)
        elif self.num == 3:
            self.labyrinth.render(screen, 3)
            self.hero.render(screen)
            self.enemy_1.render(screen)
            self.enemy_2.render(screen)

    def update_hero(self):
        next_x, next_y = self.hero.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            next_y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            next_y += 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.hero.set_position((next_x, next_y))

    def move_enemy(self):
        if self.enemy_2 == 0:
            next_position = self.labyrinth.find_path_step(
                self.enemy_1.get_position(),
                self.hero.get_position())
            self.enemy_1.set_position(next_position)
        else:
            next_position = self.labyrinth.find_path_step(
                self.enemy_1.get_position(),
                self.hero.get_position(), self.enemy_2.get_position())
            self.enemy_1.set_position(next_position)
            next_position = self.labyrinth.find_path_step(
                self.enemy_2.get_position(),
                self.hero.get_position())
            self.enemy_2.set_position(next_position)

    def check_win(self):
        return self.labyrinth.get_tile_id(
            self.hero.get_position()) == self.labyrinth.finish_tile

    def check_lose(self):
        if self.enemy_2 == 0:
            return self.hero.get_position() == self.enemy_1.get_position()
        else:
            return self.hero.get_position() == self.enemy_1.get_position() or\
                   self.hero.get_position() == self.enemy_2.get_position()


#анимация в лабиринте
class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.velocity = [dx, dy]
        self.gravity = 1
        self.fire = [load_image('finish.png', -1)]
        for scale in (5, 10, 15, 20):
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


#карта шутера
class Shooter:
    def __init__(self):
        self.background = load_image("road.png").convert()
        self.background_rect = self.background.get_rect()
        self.restart = load_image("restart.png")
        self.pause = load_image("pause.png")
        self.home = load_image("home.png")

    def render(self, screen):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.restart, (760, 10))
        screen.blit(self.pause, (760, 80))
        screen.blit(self.home, (760, 150))


#управляемый герой в шутере
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("car.png", -1)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH_2 / 2
        self.rect.bottom = HEIGHT_2 - 10
        self.speed_x = 0
        self.score = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -22
        if key_state[pygame.K_RIGHT]:
            self.speed_x = 22
        if key_state[pygame.K_UP]:
            self.speed_y = -22
        if key_state[pygame.K_DOWN]:
            self.speed_y = 22
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH_2 - 70:
            self.rect.right = WIDTH_2 - 70
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT_2:
            self.rect.bottom = HEIGHT_2

    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top + 29)
        all_sprites.add(bullet)
        bullets.add(bullet)


#противники в шутере
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("car_2.png ", -1)
        self.rect = self.image.get_rect()
        self.speedy = 8
        self.rect.x = random.randrange(WIDTH_2 - self.rect.width - 70)
        self.rect.y = random.randrange(-800, 0)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT_2:
            self.rect.x = random.randrange(WIDTH_2 - self.rect.width - 70)
            self.rect.y = random.randrange(-800, 0)
            self.speedy = 8
            sp.append(1)


#стреляние в шутере
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bul.png", -1)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -25

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


#управляемый герой в платформере
class Player_pl(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvl = 0
        self.startX = x
        self.startY = y
        self.yvl = 0
        self.onGround = False
        self.image = load_image("mush.png", -1)
        self.rect = Rect(x, y, 40, 40)
        self.flag = False

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvl = -9
        if left:
            self.xvl = -5
        if right:
            self.xvl = 5
        if not (left or right):
            self.xvl = 0
        if not self.onGround:
            self.yvl += GRAVITY
        if not self.onGround:
            self.yvl += GRAVITY
        self.onGround = False
        self.rect.y += self.yvl
        self.collide(0, self.yvl, platforms)
        self.rect.x += self.xvl
        self.collide(self.xvl, 0, platforms)

    def collide(self, xvl, yvl, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, BlockDie) or isinstance(p, Monster)\
                        or isinstance(p, Lava):
                    self.die()
                if xvl > 0:
                    self.rect.right = p.rect.left
                if xvl < 0:
                    self.rect.left = p.rect.right
                if yvl > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvl = 0
                if yvl < 0:
                    self.rect.top = p.rect.bottom
                    self.yvl = 0

    def teleporting(self, gx, gy):
        self.rect = Rect(gx, gy, 40, 40)

    def die(self):
        time.wait(800)
        self.teleporting(self.startX, self.startY)


#монстр в платформере
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, left, max_left, max_right):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("monster.png", -1)
        self.rect = Rect(x, y, 47, 55)
        self.startX = x
        self.startY = y
        self.max_left = max_left
        self.max_right = max_right
        self.xvl = left

    def update(self, platforms):
        self.rect.x += self.xvl
        self.collide(platforms)
        if (abs(self.startX - self.rect.x) > self.max_left):
            self.xvl = -2
        if (abs(self.startX - self.rect.x) < self.max_right):
            self.xvl = 2

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
                self.xvl = - self.xvl


#блоки в платформере
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Surface((39, 39))
        self.image = image.load("data/block.png")
        self.rect = Rect(x, y, 39, 39)


#колючки в платформере
class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = load_image("danger.png", -1)
        self.rect = Rect(x, y, 69, 72)


#финишная линия в платформере
class Finish(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = load_image("win.png", -1)
        self.rect = Rect(x, y, 0, 0)


#блоки лавы в платформере
class Lava(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = load_image("lava.png", -1)
        self.rect = Rect(x, y, 39, 39)


#камера в платформере
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


#работа с камерой в платформере
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + win_width / 2, -t + win_height / 2
    l = min(0, l)
    l = max(-(camera.width - win_width), l)
    t = max(-(camera.height - win_height), t)
    t = min(0, t)
    return Rect(l, t, w, h)


#работа с анимацией в лабиринте
def create_particles(position):
        sm = 13
        numbers = range(-60, 60)
        for _ in range(sm):
            Particle(position, random.choice(numbers), random.choice(numbers))


#работа с лучшим результатом в шутере
def best_result(f):
    lines = f.read().splitlines()
    lines.sort(reverse=True)
    for i in range(len(lines)):
        if len(lines[i]) == 4:
            return lines[i]


#сохраняет результат из шутера
def save_result(f, res):
    f.write('\n' + str(res))


#высвечивает сообщение
def show_message(screen, message):
    f = pygame.font.Font(None, 50)
    text = f.render(message, 1, (10, 80, 0))
    text_x = WINDOW_WIDTH // 2 - text.get_width() // 2
    text_y = WINDOW_HEIGHT // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(screen, (225, 150, 0), (text_x - 10, text_y - 10,
                                             text_w + 20, text_h + 20))
    screen.blit(text, (text_x, text_y))


#высвечивает текст
def draw_text(surf, message, x, y):
    f = pygame.font.SysFont('serif bold', 45)
    text = f.render(message, True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text, text_rect)


#загружает картинку
def load_image(name, color_key=None):
    fullname = os.path.join('DATA', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


#стартовое окно перед лабиринтом
def start_screen(screen, clock, num):
    intro_text = []
    result_text = []
    if num == 1:
        intro_text = ["              Лабиринт",
                      " ",
                      " *Соберите 3 звезды,",
                      "  чтобы найти жёлтый выход",
                      " *Не дайте красному кругу",
                      "  вас догнать"]
        result_text = ["*Для паузы нажмите",
                       " на клавиатуре 'S'"]
    elif num == 2:
        intro_text = ["              Лабиринт",
                      " ",
                      " *Соберите 4 звезды,",
                      "  чтобы найти жёлтый выход",
                      " *Не дайте красному кругу",
                      "  вас догнать"]
        result_text = ["*Для паузы нажмите",
                       " на клавиатуре 'S'"]
    elif num == 3:
        intro_text = ["              Лабиринт",
                      " ",
                      " *Соберите 5 звёзд,",
                      "  чтобы найти жёлтый выход",
                      " *Не дайте красному кругу",
                      "  вас догнать"]
        result_text = ["*Для паузы нажмите",
                       " на клавиатуре 'S'"]
    go_back_1 = "<"
    go_back_2 = "--"
    fon = pygame.transform.scale(load_image('labyrinth.png'), (850, 550))
    screen.blit(fon, (0, 0))
    f = pygame.font.Font(None, 33)
    text_coord_1 = 200
    text_coord_2 = 260
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 40, 40))
    string_rendered_1 = f.render(go_back_1, 1, pygame.Color('black'))
    screen.blit(string_rendered_1, (7, 7))
    string_rendered_2 = f.render(go_back_2, 1, pygame.Color('black'))
    screen.blit(string_rendered_2, (20, 8))
    for line in intro_text:
        string_rendered = f.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_1 += 10
        intro_rect.top = text_coord_1
        intro_rect.x = 10
        text_coord_1 += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in result_text:
        string_rendered = f.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_2 += 10
        intro_rect.top = text_coord_2
        intro_rect.x = 570
        text_coord_2 += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 40:
                    if 0 < mouse[1] < 40:
                        second_labyrinth()
            if ev.type == pygame.QUIT:
                terminate()
            elif ev.type == pygame.KEYDOWN or\
                    ev.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


#стартовое окно перед шутером
def start_screen_2(screen, clock):
    f = open("DATA/shooter_results.txt")
    mes = best_result(f)
    intro_text = ["        Шутер",
                  "*Набирайте очки,",
                  " стреляя в серые",
                  " машины(стрельба -",
                  " пробел)"]
    result_text = ["*Игра закончится,",
                   " когда вы коснётесь",
                   " серой машины или",
                   " пропустите 10 машин"]
    sum_text = [f"Лучший результа:  {mes}"]
    go_back_1 = "<"
    go_back_2 = "--"
    fon = pygame.transform.scale(load_image('back.png'), (820, 550))
    screen.blit(fon, (0, 0))
    f = pygame.font.Font(None, 33)
    text_coord_1 = 95
    text_coord_2 = 325
    text_coord_3 = 300
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 40, 40))
    string_rendered_1 = f.render(go_back_1, 1, pygame.Color('black'))
    screen.blit(string_rendered_1, (7, 7))
    string_rendered_2 = f.render(go_back_2, 1, pygame.Color('black'))
    screen.blit(string_rendered_2, (20, 8))
    for line in intro_text:
        string_rendered = f.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_1 += 10
        intro_rect.top = text_coord_1
        intro_rect.x = 10
        text_coord_1 += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in result_text:
        string_rendered = f.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_2 += 10
        intro_rect.top = text_coord_2
        intro_rect.x = 170
        text_coord_2 += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    for line in sum_text:
        string_rendered = f.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord_3 += 10
        intro_rect.top = text_coord_3
        intro_rect.x = 430
        text_coord_3 += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 40:
                    if 0 < mouse[1] < 40:
                        first()
            if ev.type == pygame.QUIT:
                terminate()
            elif ev.type == pygame.KEYDOWN or\
                    ev.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


#стартовое окно платформером
def start_screen_3(screen, clock):
    intro_text = ["             Платформер",
                  "-Дойдите до конца карты",
                  "-Нельзя соприкасаться с",
                  " шипами, монстром и лавой"]
    go_back_1 = "<"
    go_back_2 = "--"
    fon = pygame.transform.scale(load_image('fon_2.png'), (830, 610))
    screen.blit(fon, (0, 0))
    f = pygame.font.Font(None, 40)
    text_coord_1 = 270
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 40, 40))
    string_rendered_1 = f.render(go_back_1, 1, pygame.Color('black'))
    screen.blit(string_rendered_1, (7, 7))
    string_rendered_2 = f.render(go_back_2, 1, pygame.Color('black'))
    screen.blit(string_rendered_2, (20, 8))
    for line in intro_text:
        string_rendered = f.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord_1 += 12
        intro_rect.top = text_coord_1
        intro_rect.x = 220
        text_coord_1 += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 40:
                    if 0 < mouse[1] < 40:
                        first()
            if ev.type == pygame.QUIT:
                terminate()
            elif ev.type == pygame.KEYDOWN or\
                    ev.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


#новые противники в шутере
def new_mob(sprites, mobs):
    m = Mob()
    sprites.add(m)
    mobs.add(m)


#выход из игры
def terminate():
    pygame.quit()
    sys.exit()


#запуск лёгкого уровня лабиринта
def labyrinth_easy():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Лабиринт')
    hero = Hero((1, 1))
    enemy = Enemy((11, 8), 1)
    labyrinth = Labyrinth('map.txt', [0, 2], 2, hero, 1)
    game = Game(labyrinth, hero, enemy, 1)
    clock = pygame.time.Clock()
    start_screen(screen, clock, 1)
    running = True
    game_over = False
    pause = False
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 12 < mouse[0] < 69:
                    if 469 < mouse[1] < 525:
                        labyrinth_easy()
                elif 149 < mouse[0] < 201:
                    if 469 < mouse[1] < 518:
                        first()
                elif 79 < mouse[0] < 131:
                    if 469 < mouse[1] < 521:
                        if pause is False:
                            pause = True
                        else:
                            pause = False
            if ev.type == pygame.QUIT:
                terminate()
            if ev.type == ENEMY_EVENT_TYPE and not game_over and\
                    pause is False:
                game.move_enemy()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]:
            if pause is False:
                pause = True
            else:
                pause = False
        if not game_over and pause is False:
            game.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        if pause:
            show_message(screen, 'ПАУЗА')
        if game.check_win():
            game_over = True
            show_message(screen, 'ПОБЕДА!')
            create_particles((400, 0))
        if game.check_lose():
            game_over = True
            show_message(screen, 'ВЫ ПРОИГРАЛИ!')
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


#запуск среднего уровня лабиринта
def labyrinth_medium():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Лабиринт')
    hero = Hero((19, 12))
    enemy_1 = Enemy((4, 5), 2)
    enemy_2 = Enemy((21, 6), 2)
    labyrinth = Labyrinth('map_2.txt', [0, 2], 2, hero, 2)
    game = Game(labyrinth, hero, enemy_1, 2, enemy_2)
    clock = pygame.time.Clock()
    start_screen(screen, clock, 2)
    running = True
    game_over = False
    pause = False
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 12 < mouse[0] < 69:
                    if 469 < mouse[1] < 525:
                        labyrinth_medium()
                elif 149 < mouse[0] < 201:
                    if 469 < mouse[1] < 518:
                        first()
                elif 79 < mouse[0] < 131:
                    if 469 < mouse[1] < 521:
                        if pause is False:
                            pause = True
                        else:
                            pause = False
            if ev.type == pygame.QUIT:
                terminate()
            if ev.type == ENEMY_EVENT_TYPE and not game_over and\
                    pause is False:
                game.move_enemy()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]:
            if pause is False:
                pause = True
            else:
                pause = False
        if not game_over and pause is False:
            game.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        if pause:
            show_message(screen, 'ПАУЗА')
        if game.check_win():
            game_over = True
            show_message(screen, 'ПОБЕДА!')
            create_particles((400, 0))
        if game.check_lose():
            game_over = True
            show_message(screen, 'ВЫ ПРОИГРАЛИ!')
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


#запуск сложного уровня лабиринта
def labyrinth_hard():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Лабиринт')
    hero = Hero((15, 1))
    enemy_1 = Enemy((24, 3), 3)
    enemy_2 = Enemy((12, 7), 3)
    labyrinth = Labyrinth('map_3.txt', [0, 2], 2, hero, 3)
    game = Game(labyrinth, hero, enemy_1, 3, enemy_2)
    clock = pygame.time.Clock()
    start_screen(screen, clock, 3)
    running = True
    game_over = False
    pause = False
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 12 < mouse[0] < 69:
                    if 469 < mouse[1] < 525:
                        labyrinth_hard()
                elif 149 < mouse[0] < 201:
                    if 469 < mouse[1] < 518:
                        first()
                elif 79 < mouse[0] < 131:
                    if 469 < mouse[1] < 521:
                        if pause is False:
                            pause = True
                        else:
                            pause = False
            if ev.type == pygame.QUIT:
                terminate()
            if ev.type == ENEMY_EVENT_TYPE and not game_over and\
                    pause is False:
                game.move_enemy()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]:
            if pause is False:
                pause = True
            else:
                pause = False
        if not game_over and pause is False:
            game.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        if pause:
            show_message(screen, 'ПАУЗА')
        if game.check_win():
            game_over = True
            show_message(screen, 'ПОБЕДА!')
            create_particles((400, 0))
        if game.check_lose():
            game_over = True
            show_message(screen, 'ВЫ ПРОИГРАЛИ!')
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


#запуск шутера
def shooter_easy():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH_2, HEIGHT_2))
    pygame.display.set_caption("Шутер")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    shooter = Shooter()
    player = Player()
    bullets = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    all_sprites.add(player)
    start_screen_2(screen, clock)
    f = open("DATA/shooter_results.txt", "a")
    game_over = False
    pause = False
    running = True
    game = True
    while running:
        if game:
            game = False
            del sp[:-1]
            for i in range(8):
                new_mob(all_sprites, mobs)
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 9 < mouse[1] < 64:
                    if 759 < mouse[0] < 815:
                        del sp[:len(sp)]
                        shooter_easy()
                elif 149 < mouse[1] < 201:
                    if 759 < mouse[0] < 811:
                        del sp[:len(sp)]
                        first()
                elif 79 < mouse[1] < 128:
                    if 759 < mouse[0] < 811:
                        if pause is False:
                            pause = True
                        else:
                            pause = False
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE and game_over is False and\
                        pause is False:
                    player.shoot(all_sprites, bullets)
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            player.score += 30
            new_mob(all_sprites, mobs)
        hits = pygame.sprite.spritecollide(player, mobs, False)
        screen.fill((0, 0, 0))
        shooter.render(screen)
        draw_text(screen, f'ОЧКИ: {str(player.score)}', 640, 10)
        draw_text(screen, f'ПРОПУСКИ: {str(len(sp))}/10 ', 150, 10)
        if pause:
            show_message(screen, 'ПАУЗА')
        if hits:
            if game_over is False:
                save_result(f, player.score)
            game_over = True
            show_message(screen, 'КОНЕЦ ИГРЫ')
        if len(sp) == 10:
            if game_over is False:
                save_result(f, player.score)
                game_over = True
            show_message(screen, 'КОНЕЦ ИГРЫ')
        if not pause and not game_over:
            all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


#запуск платформера
def platform_easy():
    pygame.init()
    screen = pygame.display.set_mode(win_size)
    pygame.display.set_caption("Платформер")
    bg = Surface((win_width, win_height))
    bg.fill(Color('#00BFFF'))
    pygame.draw.rect(bg, (0, 0, 0), (0, 540, 830, 70))
    hero = Player_pl(60, 70)
    mn_1 = Monster(42, 450, 2, 1550, 30)
    home = load_image("home.png")
    bg.blit(home, (13, 555))
    left = right = False
    up = False
    platforms = []
    timer = pygame.time.Clock()
    start_screen_3(screen, timer)
    width = 39
    height = 39
    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "+":
                lv = Lava(x, y)
                entities.add(lv)
                platforms.append(lv)
            x += width
        y += height
        x = 0
    fn = Finish(2495, 249)
    entities.add(fn)
    platforms.append(fn)
    total_level_width = len(level[0]) * width
    total_level_height = len(level) * height
    camera = Camera(camera_configure, total_level_width, total_level_height)
    game_over = False
    game = True
    running = True
    while running:
        if game:
            game = False
            monsters.add(mn_1)
            platforms.append(mn_1)
            entities.add(hero)
            entities.add(mn_1)
        timer.tick(60)
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 12 < mouse[0] < 64:
                    if 554 < mouse[1] < 603:
                        first()
            if ev.type == QUIT:
                terminate()
            if ev.type == KEYDOWN and ev.key == K_UP:
                up = True
            if ev.type == KEYDOWN and ev.key == K_LEFT:
                left = True
            if ev.type == KEYDOWN and ev.key == K_RIGHT:
                right = True
            if ev.type == KEYUP and ev.key == K_UP:
                up = False
            if ev.type == KEYUP and ev.key == K_RIGHT:
                right = False
            if ev.type == KEYUP and ev.key == K_LEFT:
                left = False
        screen.blit(bg, (0, 0))
        camera.update(hero)
        if game_over is False:
            monsters.update(platforms)
            hero.update(left, right, up, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()


#запуск экрана с выбором уровня в лабиринте
def second_labyrinth():
    pygame.init()
    second_window = pygame.display.set_mode((250, 350))
    pygame.display.set_caption('Choose')
    background = pygame.Surface((250, 350))
    background.fill(pygame.Color("#FFE4C4"))
    manager = pygame_gui.UIManager((250, 350))
    f = pygame.font.SysFont('serif', 30)
    text_1 = f.render("ВЫБЕРЕТЕ", False, (0, 0, 0))
    text_2 = f.render("СЛОЖНОСТЬ", False, (0, 0, 0))
    background.blit(text_1, (50, 20))
    background.blit(text_2, (32, 55))
    open_labyrinth_easy = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((55, 115), (140, 42)),
        text='Лёгкий',
        manager=manager
    )
    open_labyrinth_medium = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((55, 185), (140, 42)),
        text='Средний',
        manager=manager
    )
    open_labyrinth_hard = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((55, 255), (140, 42)),
        text='Сложный',
        manager=manager
    )
    go_back = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((0, 0), (33, 33)),
        text='<--',
        manager=manager
    )
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(60) / 1000.0
        for event_2 in pygame.event.get():
            if event_2.type == pygame.QUIT:
                terminate()
            if event_2.type == pygame.USEREVENT:
                if event_2.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event_2.ui_element == open_labyrinth_easy:
                        labyrinth_easy()
                    elif event_2.ui_element == open_labyrinth_medium:
                        labyrinth_medium()
                    elif event_2.ui_element == open_labyrinth_hard:
                        labyrinth_hard()
                    elif event_2.ui_element == go_back:
                        first()
            manager.process_events(event_2)
        manager.update(time_delta)
        second_window.blit(background, (0, 0))
        manager.draw_ui(second_window)
        pygame.display.update()


#стартовое окно
def first():
    pygame.init()
    window = pygame.display.set_mode((850, 550))
    pygame.display.set_caption('Start')
    f_1 = pygame.font.SysFont('serif', 60)
    f_2 = pygame.font.SysFont('serif', 30)
    text = f_1.render("ВЫБЕРЕТЕ ИГРУ", False, (0, 0, 0))
    name_1 = f_2.render("ЛАБИРИНТ", False, (0, 0, 0))
    name_2 = f_2.render("ПЛАТФОРМЕР", False, (0, 0, 0))
    name_3 = f_2.render("ШУТЕР", False, (0, 0, 0))
    logo = load_image("logo.png", -1)
    game_1 = load_image("game_1.png")
    game_2 = load_image("game_2.png")
    game_3 = load_image("game_3.png")
    background = pygame.Surface((850, 550))
    background.fill(pygame.Color('#FFE4C4'))
    background.blit(logo, (650, 0))
    background.blit(game_1, (70, 247))
    background.blit(game_2, (335, 247))
    background.blit(game_3, (600, 247))
    background.blit(text, (30, 30))
    background.blit(name_1, (80, 200))
    background.blit(name_2, (325, 200))
    background.blit(name_3, (640, 200))
    manager = pygame_gui.UIManager((850, 550))
    open_labyrinth_level = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((70, 450), (180, 42)),
        text='Выбрать',
        manager=manager
    )
    open_platform_level = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((335, 450), (180, 42)),
        text='Выбрать',
        manager=manager
    )
    open_shooter = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((600, 450), (180, 42)),
        text='Выбрать',
        manager=manager
    )
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(60) / 1000.0
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                dialog = pygame_gui.windows.UIConfirmationDialog(
                    rect=pygame.Rect((275, 100), (300, 200)),
                    manager=manager,
                    window_title='Подтверждение',
                    action_long_desc='Вы уверены, что хотите выйти?',
                    action_short_name='OK',
                    blocking=True
                )
            if ev.type == pygame.USEREVENT:
                if ev.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                    terminate()
                if ev.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if ev.ui_element == open_labyrinth_level:
                        second_labyrinth()
                    elif ev.ui_element == open_shooter:
                        shooter_easy()
                    elif ev.ui_element == open_platform_level:
                        platform_easy()
            manager.process_events(ev)
        manager.update(time_delta)
        window.blit(background, (0, 0))
        manager.draw_ui(window)
        pygame.display.update()


if __name__ == '__main__':
    first()
