import time
import sys
import pygame
from pygame import mixer
from pygame.locals import *
from Key import *
from Song import *
from Flote import *

pygame.init()
pygame.mixer.init()
# add white keys
board = [Key("\t", 1, "cOne", "beautiful_sounds/mp3_Notes/c3.mp3"),
         Key("q", 2, "dOne", "beautiful_sounds/mp3_Notes/d3.mp3"),
         Key("w", 3, "eOne", "beautiful_sounds/mp3_Notes/e3.mp3"),
         Key("e", 4, "fOne", "beautiful_sounds/mp3_Notes/f3.mp3"),
         Key("r", 5, "gOne", "beautiful_sounds/mp3_Notes/g3.mp3"),
         Key("t", 6, "aOne", "beautiful_sounds/mp3_Notes/a4.mp3"),
         Key("y", 7, "bOne", "beautiful_sounds/mp3_Notes/b4.mp3"),
         Key("u", 8, "cTwo", "beautiful_sounds/mp3_Notes/c4.mp3"),
         Key("i", 9, "dTwo", "beautiful_sounds/mp3_Notes/d4.mp3"),
         Key("o", 10, "eTwo", "beautiful_sounds/mp3_Notes/e4.mp3"),
         Key("p", 11, "fTwo", "beautiful_sounds/mp3_Notes/f4.mp3"),
         Key("[", 12, "gTwo", "beautiful_sounds/mp3_Notes/g4.mp3"),
         Key("]", 13, "aTwo", "beautiful_sounds/mp3_Notes/a5.mp3"),
         Key("\\", 14, "bTwo", "beautiful_sounds/mp3_Notes/b5.mp3")]

# add black keys
blackboard = [Key("1", 1, "cArp", "beautiful_sounds/mp3_Notes/c-3.mp3"),
              Key("2", 2, "dArp", "beautiful_sounds/mp3_Notes/d-3.mp3"),
              Key("4", 4, "fArp", "beautiful_sounds/mp3_Notes/f-3.mp3"),
              Key("5", 5, "gArp", "beautiful_sounds/mp3_Notes/g-3.mp3"),
              Key("6", 6, "aArp", "beautiful_sounds/mp3_Notes/a-4.mp3"),
              Key("8", 8, "cArp2", "beautiful_sounds/mp3_Notes/c-4.mp3"),
              Key("9", 9, "dArp2", "beautiful_sounds/mp3_Notes/d-4.mp3"),
              Key("-", 11, "fArp2", "beautiful_sounds/mp3_Notes/f-4.mp3"),
              Key("=", 12, "gArp2", "beautiful_sounds/mp3_Notes/g-4.mp3"),
              Key("\b", 13, "aArp2", "beautiful_sounds/mp3_Notes/a-5.mp3")]

# set screen size

screen_height = 640
screen_width = 960

# set screen to display at size
screen = pygame.display.set_mode((screen_width, screen_height))

# set tag to Pyano
pygame.display.set_caption('Pyano')

back_img = pygame.image.load("images_for_pyano/pyano_back.jpg")


def insrtButton(red, green, blue, text, rect, xCord, yCord):
    white = (255, 255, 255)
    incolor = (red, green, blue)
    font = pygame.font.SysFont('Arial', 30)
    pygame.draw.rect(screen, incolor, rect)
    screen.blit(font.render(text, True, white), (xCord, yCord))


# define and run menu screen
def menu():
    while True:

        screen.fill((255, 255, 255))

        mouseX, mouseY = pygame.mouse.get_pos()
        buttonSong = pygame.Rect(300, 460, 20, 40)
        insrtButton(51, 208, 255, "Play song", buttonSong, 300, 460)

        if buttonSong.collidepoint((mouseX, mouseY)):
            if click:
                game()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

    pygame.display.update()


menu()


def game():
    running = True
    marysheet = Song("aaaaaaa")
    marysheet.compose()
    while running:

        sounds = []

        # Display auditorium
        screen.blit(back_img, (0, 0))

        # make corner x quit out
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # color creation
        white = (255, 255, 255)
        red = (200, 30, 30)
        black = (0, 0, 0)
        blue = (20, 50, 250)
        purple = (255, 0, 255)

        # draw white keys
        for Key in board:
            x_start = 60 * Key.location
            y_start = 530
            y_height = 110
            x_width = 50

            if Key.struck():
                pygame.draw.rect(screen, red, [x_start, y_start, x_width, y_height])
                mixer.music.load(Key.sound)
                sound = pygame.mixer.Sound(Key.sound)
                sound.set_volume(100)
                sounds.append(sound)
            else:
                pygame.draw.rect(screen, white, [x_start, y_start, x_width, y_height])

        # draw black keys
        for Key in blackboard:
            x_start2 = ((60 * Key.location) + 40)
            y_start2 = 530
            y_height2 = 60
            x_width2 = 30

            if Key.struck():
                pygame.draw.rect(screen, blue, [x_start2, y_start2, x_width2, y_height2])
                mixer.music.load(Key.sound)
                sound = pygame.mixer.Sound(Key.sound)
                sound.set_volume(100)
                sounds.append(sound)
            else:
                pygame.draw.rect(screen, black, [x_start2, y_start2, x_width2, y_height2])

            # draw floaters

        for k in marysheet:
            if (k.loc <= 14):
                x_start2 = (60 * k.loc)
                y_start2 = k.height
                y_length2 = 20
                x_width2 = 50
            elif (k.loc > 14):
                x_start2 = (60 * (k.loc - 14) + 40)
                y_start2 = k.height
                y_length2 = 20
                x_width2 = 30
            if (y_start2 < 531):
                pygame.draw.rect(screen, purple, [x_start2, y_start2, x_width2, y_length2])

        for k in marysheet:
            if k.height != 1000 & k.height != 2000:
                k.setHeight(k.height + 5)
        time.sleep(0.035)

        for Key in board:
            for k in marysheet:
                if Key.key == k.button and k.height and 500 and k.height < 530 and Key.struck():
                    marysheet.remove(k)

        length = len(marysheet)
        if marysheet[-1].height == 1000:
            for i in range(length - 1):
                if (marysheet[i].key != " "):
                    if marysheet[i].height == 30:
                        if marysheet[i + 1].button != 'N':
                            marysheet[i + 1].setHeight(0)
                            i += 1
                    elif marysheet[i].height == 60:
                        if marysheet[i + 1].button == "N":
                            marysheet[i + 2].setHeight(0)
                            i += 1
                    else:
                        i += 1
                else:
                    i += 1

        if len(sounds) != 0:
            pygame.mixer.music.stop()
            for object in sounds:
                object.play()

        pygame.display.update()


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()

#testing