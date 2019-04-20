# coding=utf-8
"""
EXAMPLE 2
Game menu with 3 difficulty options.

Copyright (C) 2017-2018 Pablo Pizarro @ppizarror

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# Import pygame and libraries
# from locals import *
from pygame.locals import *
from random import randrange
import os
import pygame
from game import main

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

ABOUT = ['Author:',
         "Natural   gay'ms",
         PYGAMEMENU_TEXT_NEWLINE,
         'Name:   Space   ships']
HELP = ['Boost:    Spase',
         'Left  rotation:    a',
         'Right  rotation:    d']
COLOR_BACKGROUND = (128, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (30, 30, 30)
COLOR_LIGHT_GRAY = (50, 50, 50)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (640, 480)

# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('PygameMenu example 2')
clock = pygame.time.Clock()
dt = 1 / FPS


# -----------------------------------------------------------------------------


def play_function():
    main()


def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    surface.fill(COLOR_GRAY)


# -----------------------------------------------------------------------------
# PLAY MENU
play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_LIGHT_GRAY,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
# When pressing return -> play(DIFFICULTY[0], font)
play_menu.add_option('Start', play_function,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_WHITE,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=COLOR_LIGHT_GRAY,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_WHITE,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# MAIN MENU
help_menu= pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_WHITE,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=COLOR_LIGHT_GRAY,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_WHITE,
                                 text_fontsize=20,
                                 title='Help',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )

for m in HELP:
    help_menu.add_line(m)
help_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
help_menu.add_option('Return to menu', PYGAME_MENU_BACK)
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_WHITE,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=COLOR_BLACK,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )

main_menu.add_option('Play', play_function)
main_menu.add_option('About', about_menu)
main_menu.add_option('Help', help_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
# Main loop
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()
