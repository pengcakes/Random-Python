"""
AP
Needs:
/Constant update of GUI --- scroll to left + gravity
/Pipe Objects --- only ever 2 sets of pipes ( 2 at a time)
/Bird Object
/Collision Detection
/Keyboard Input
Score Keeping -- save highscores?? (for AI)
Allow multiple birds (for AI)
"""
import math
import os
from random import randint
import pygame
from pygame.locals import *
import ai

######################################################
SCREEN_W = 400
SCREEN_H = 400
PIPE_W = 30
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
font_name = pygame.font.match_font('arial')
FIRST_RUN = True
DISTANCE_TRAVELED = 0
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
MOVE_SPEED = 2

SCORE = 0
bird_size = 30
bird_color = BLUE
bx = 60
by = SCREEN_H/2 - 30
#column stuff
top_col_height = 140
bot_col_height = -140
difficulty = 90
rand_difference = randint(-difficulty, difficulty)
rand_difference2 = randint(-difficulty, difficulty)
topx = botx = SCREEN_W
topy = 0
boty = SCREEN_H 

topx2 = botx2 = SCREEN_W
topy2 = 0
boty2 = SCREEN_H 
#sprites
player = pygame.sprite.Sprite()
column = pygame.sprite.Sprite()
column2 = pygame.sprite.Sprite()
column3 = pygame.sprite.Sprite()
column4 = pygame.sprite.Sprite()
######################################################


def bird_maker():
	player.rect = pygame.draw.rect(screen, bird_color, pygame.Rect(bx, by, bird_size, bird_size))

def onHit(s1, s2):
        return pygame.sprite.collide_rect(s1, s2)

def col_maker():
	column.rect = pygame.draw.rect(screen, GREEN, pygame.Rect(topx, topy, PIPE_W, top_col_height+rand_difference))

	column2.rect = pygame.draw.rect(screen, GREEN, pygame.Rect(botx, boty, PIPE_W, bot_col_height+rand_difference))

def col_maker2():
        column3.rect = pygame.draw.rect(screen, RED, pygame.Rect(topx2, topy2, PIPE_W, top_col_height+rand_difference2))

        column4.rect = pygame.draw.rect(screen, RED, pygame.Rect(botx2, boty2, PIPE_W, bot_col_height+rand_difference2))

def pause():
        pause = True
        while pause == True:
                pressed = pygame.key.get_pressed()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return True
                                break
                if pressed[pygame.K_q]:
                        return True
                        break
                if pressed[pygame.K_r]:
                        return False
                        break

def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

def main():
        global bx, by, topx, botx, topx2, botx2, done, SCORE, rand_difference, FIRST_RUN, DISTANCE_TRAVELED

        pygame.init()
        pygame.display.set_caption("Discount Flap Game")
        clock = pygame.time.Clock()
        done = False

        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE] or pressed[pygame.K_UP]: by -= MOVE_SPEED+10
                #background
                screen.fill((0, 0, 0))
                #gravity & animations
                by+=MOVE_SPEED
                topx-=MOVE_SPEED
                botx-=MOVE_SPEED
                
                bird_maker()
                col_maker()
                
                if FIRST_RUN:
                        if topx < SCREEN_W/2:
                                col_maker2()
                                topx2-=MOVE_SPEED
                                botx2-=MOVE_SPEED
                
                if not FIRST_RUN:
                        col_maker2()
                        topx2-=MOVE_SPEED
                        botx2-=MOVE_SPEED
                #new columns
                if topx == 0:
                        topx = botx = SCREEN_W
                        topy = 0
                        boty = SCREEN_H
                        rand_difference = randint(-difficulty, difficulty)
                        FIRST_RUN = False
                if topx2 == 0:
                        topx2 = botx2 = SCREEN_W
                        topy2 = 0
                        boty2 = SCREEN_H
                        rand_difference2 = randint(-difficulty, difficulty)

                #score counter
                if topx == bx or topx2 == bx:
                        SCORE+=1
                #collisions
                if FIRST_RUN:
                        if onHit(player, column) or onHit(player, column2) or by >= SCREEN_H - bird_size or by <= 0:
                                draw_text(screen, "Game Over", 32, SCREEN_W / 2, SCREEN_H / 2-40)
                                draw_text(screen, "Press R to RESTART", 22, SCREEN_W / 2, SCREEN_H / 2)
                                draw_text(screen, "Press Q to QUIT", 22, SCREEN_W / 2, SCREEN_H / 2 + 20)
                                pygame.display.flip()  
                                if pause() == True:
                                        done = True
                                if pause() == False:
                                        SCORE = 0
                                        DISTANCE_TRAVELED = 0
                                        FIRST_RUN = True
                                        bx = 60
                                        by = SCREEN_H/2 - 30
                                        topx=botx=topx2=botx2=SCREEN_W
                                        rand_difference = randint(-difficulty, difficulty)
                                        rand_difference2 = randint(-difficulty, difficulty)
                                        main()
                if not FIRST_RUN:
                        if onHit(player, column) or onHit(player, column2) or onHit(player, column3) or onHit(player, column4) or by >= SCREEN_H - bird_size or by <= 0:
                                draw_text(screen, "Game Over", 32, SCREEN_W / 2, SCREEN_H / 2-40)
                                draw_text(screen, "Press R to RESTART", 22, SCREEN_W / 2, SCREEN_H / 2)
                                draw_text(screen, "Press Q to QUIT", 22, SCREEN_W / 2, SCREEN_H / 2 + 20)
                                pygame.display.flip()  
                                if pause() == True:
                                        done = True
                                if pause() == False:
                                        SCORE = 0
                                        DISTANCE_TRAVELED = 0
                                        FIRST_RUN = True
                                        bx = 60
                                        by = SCREEN_H/2 - 30
                                        topx=botx=topx2=botx2=SCREEN_W
                                        rand_difference = randint(-difficulty, difficulty)
                                        rand_difference2 = randint(-difficulty, difficulty)
                                        main()
                #score
                draw_text(screen, str(SCORE), 32, SCREEN_W / 2, SCREEN_H - 380)
                DISTANCE_TRAVELED+=1
                draw_text(screen, 'Distance: '+ str(DISTANCE_TRAVELED), 18, 50, SCREEN_H - 380)
                #updates screen
                pygame.display.flip()   
                #60fps bb
                clock.tick(60)


if __name__ == "__main__":
	main()
