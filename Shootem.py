#plane shooting game

import os, pygame, sys
import Menus

os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()

import GlobVar
GlobVar.initialize()

pygame.display.set_caption("PlaneShooter")
pygame.mouse.set_visible(0)


#Menu Music
music = pygame.mixer.music.load(GlobVar.format_path("resources/audio/house_lo.ogg"))
pygame.mixer.music.play(-1)#infinite loop of audio


over=True
Menus.mainMenu()

pygame.quit()
            
