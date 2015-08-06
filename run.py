__author__ = 'vegasq'

import copy
import os
import pygame
import random
import sys
import time


class Worm(object):
    body = [(10, 10)]
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    direction = UP

    def possible_turn(self, gamemap, new_position):
        if gamemap.gamemap[new_position[1]][new_position[0]] in [1, 2] or \
           new_position in self.body:
            return False
        return True

    def eat_star(self, gamemap, new_position):
        if gamemap.gamemap[new_position[1]][new_position[0]] in [3]:
            gamemap.gamemap[new_position[1]][new_position[0]] = 0
            self.body.append(self.body[-1])

    def step(self, gamemap):
        state = pygame.key.get_pressed()
        if state[pygame.K_UP] != 0 and self.direction != self.DOWN:
            self.direction = self.UP
        elif state[pygame.K_DOWN] != 0 and self.direction != self.UP:
            self.direction = self.DOWN
        elif state[pygame.K_LEFT] != 0 and self.direction != self.RIGHT:
            self.direction = self.LEFT
        elif state[pygame.K_RIGHT] != 0 and self.direction != self.LEFT:
            self.direction = self.RIGHT

        def go_up(x, y):
            return (x, y - 1)

        def go_down(x, y):
            return (x, y + 1)

        def go_left(x, y):
            return (x -1, y)

        def go_right(x, y):
            return (x + 1, y)

        if self.direction == self.UP:
            do = go_up
        elif self.direction == self.DOWN:
            do = go_down
        elif self.direction == self.LEFT:
            do = go_left
        elif self.direction == self.RIGHT:
            do = go_right

        if self.possible_turn(gamemap, do(*self.body[0])):
            self.eat_star(gamemap, do(*self.body[0]))
            self.body.insert(0, do(*self.body[0]))
        else:
            exit()
        del self.body[-1]
        return player


class GameMap(object):
    gamemap = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    def __init__(self):
        global screen
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill((2, 2, 2))

    def spawn_new_star(self):
        if random.randint(1, 10) == 1:
            y = len(self.gamemap)
            x = len(self.gamemap[0])
            self.gamemap[
                random.choice(range(1, y - 1))][
                random.choice(range(1, x - 1))] = 3

    def draw_map(self, player):
        self.background.fill((2, 2, 2))
        self.spawn_new_star()
        filled_map = copy.deepcopy(self.gamemap)
        for part in player.body:
            filled_map[part[1]][part[0]] = 2

        for line in filled_map:
            for row in line:
                if row == 0:
                    sys.stdout.write(' ')
                elif row == 1:
                    sys.stdout.write('+')
                elif row == 2:
                    sys.stdout.write('#')
                elif row == 3:
                    sys.stdout.write('*')
            sys.stdout.write('\n')

        font = pygame.font.Font(None, 36)
        for l, line in enumerate(filled_map):
            for r, row in enumerate(line):
                if row == 0:
                    text = font.render(" ", 1, (255, 10, 10))
                    self.background.blit(text, (r + 20 * r, l + 20 * l))
                elif row == 1:
                    text = font.render("+", 1, (255, 10, 10))
                    self.background.blit(text, (r + 20 * r, l + 20 * l))
                elif row == 2:
                    text = font.render("#", 1, (255, 255, 10))
                    self.background.blit(text, (r + 20 * r, l + 20 * l))
                elif row == 3:
                    text = font.render("*", 1, (255, 10, 255))
                    self.background.blit(text, (r + 20 * r, l + 20 * l))


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Worm')
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()

    player = Worm()
    gamemap = GameMap()

    while True:
        player.step(gamemap)
        gamemap.draw_map(player)

        screen.blit(gamemap.background, (0, 0))
        pygame.display.flip()

        clock.tick(10)
        pygame.event.pump()
