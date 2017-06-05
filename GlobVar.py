#defines the global variables
import os, pygame, Objects, sys

global width, height, screen, over, level, Name, enemyList, playerBulletList, enemyBulletList, lifeList, explosionList, lifeReceipt

dirname = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
def format_path(name):
    fullname = os.path.join(dirname, name)
    filename = fullname.replace('\\', '/')#on LINUX, comment this line, and uncomment the following line.
    #filename = fullname.replace('/', '\\')
    return filename

def reset():
    enemyList.empty()
    playerBulletList.empty()
    enemyBulletList.empty()
    lifeList.empty()
    explosionList.empty()
    lifeReceipt.empty()

def initialize():
    global width, height, screen, over, level, Name, enemyList, playerBulletList, enemyBulletList, lifeList, explosionList, lifeReceipt
    
    icon = pygame.image.load(format_path("resources/images/logo.png"))
    pygame.display.set_icon(icon)

    width = 1000
    height = 600
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

    over=True
    level=1
    Name=''

    enemyList=pygame.sprite.Group()
    playerBulletList=pygame.sprite.Group()
    enemyBulletList=pygame.sprite.Group()
    lifeList=pygame.sprite.Group()
    explosionList=pygame.sprite.Group()
    lifeReceipt=pygame.sprite.Group()
    





