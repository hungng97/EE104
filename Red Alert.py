# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 16:25:58 2022

@author: Hung
"""

import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

#Declare constants
FONT_COLOR = (255, 255, 255)
WIDTH = 1000
HEIGHT = 560
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 7
START_SPEED = 8
COLORS = ["girl", "yellow"]

#Declare global variables
game_over = False
game_complete = False
current_level = 1

#Keep track of the minions on the screen
minions = []
animations = []

# playing music
pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.play()


#Draw the minions
def draw():
    global minions, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0,0)) #add a background image to the game window
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
        for minion in minions:
            minion.draw()

def update():
    global minions, game_complete, game_over, current_level
    if len(minions) == 0:
        minions = make_minions(current_level)
    if (game_complete or game_over) and keyboard.space:
        minions = []
        current_level = 1
        game_complete = False
        game_over = False

def make_minions(number_of_extra_minions):
    colors_to_create = get_colors_to_create(number_of_extra_minions)
    new_minions = create_minions(colors_to_create)
    layout_minions(new_minions)
    animate_minions(new_minions)
    return new_minions

def get_colors_to_create(number_of_extra_minions):
    #return[]
    colors_to_create = ["evil"]
    for i in range(0, number_of_extra_minions):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_minions(colors_to_create):
    #return[]
    new_minions = []
    for color in colors_to_create:
        minion = Actor(color + "-minion")
        new_minions.append(minion)
    return new_minions

def layout_minions(minions_to_layout):
    #pass
    number_of_gaps = len(minions_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(minions_to_layout)
    for index, minion in enumerate(minions_to_layout):
        new_x_pos = (index + 1) * gap_size
        minion.x = new_x_pos
        # if index % 2 == 0:
        #     star.y = 0
        # else:
        #     star.y = HEIGHT

def animate_minions(minions_to_animate):
    #pass
    for star in minions_to_animate:
        random_speed_adjustment = random.randint(0,2)
        duration = START_SPEED - current_level + random_speed_adjustment
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)



def handle_game_over():
    global game_over
    game_over = True


def on_mouse_down(pos):
    global minions, current_level
    for minion in minions:
        if minion.collidepoint(pos):
            if "evil" in minion.image:
                evil_minion_click()
            else:
                handle_game_over()


def evil_minion_click():
    global current_level, minions, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        minions = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTER_X, CENTER_Y+30),
                     color=FONT_COLOR)

def shuffle():
    global minions
    if minions:
        x_values = [minion.x for minion in minions]
        random.shuffle(x_values)
        for index, star in enumerate(minions):
            new_x = x_values[index]
            animation = animate(star, duration=0.5, x=new_x)
            animations.append(animation)

clock.schedule_interval(shuffle, 1)

pgzrun.go()