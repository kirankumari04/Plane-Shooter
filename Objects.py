#Defines classes for game objects
import pygame, random, sys
import GlobVar


#Stars in the background
class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([GlobVar.width,GlobVar.height])
        self.image.fill(255,255,255)
        self.image.set_colorkey((255,255,255))
        pygame.draw.circle(self.image,(255,255,0),(random.randrange(GlobVar.width), random.randrange(GlobVar.height)),random.randrange(5), 0)
        self.rect=self.image.get_rect()

    def update(self):
        if self.rect.top>GlobVar.height:
            self.kill()
        else:
            self.rect.move_ip((0,2))

            
#Enemy planes
class Enemy(pygame.sprite.Sprite):
    def __init__(self, _type):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(GlobVar.format_path("resources/images/aplane"+str(_type)+".png"))
        self.rect=self.image.get_rect()
        self.type=_type
        self.spacing=0
        self.shot=-1
        self.reset()

    def reset(self):
        self.rect.x=random.randrange(GlobVar.width)
        self.rect.y=random.randrange(10)
        self.dx=random.randrange(-2,2)
        self.dy=random.randrange(2,6)

    def update(self):
        if self.shot>0:
            self.shot-=1
            if self.shot==0:
                GlobVar.enemyList.remove(self)
                self.kill()
        else:
            self.rect.x+=self.dx
            if GlobVar.over==False:
                self.rect.y+=self.dy+GlobVar.level
            else:
                self.rect.y+=self.dy+GlobVar.level-1
            if self.rect.top>GlobVar.screen.get_height():
                self.reset()
            #Enemy bullets for type 2 game
            if self.type==2:
                fire=random.randrange(3)
                if fire==0:
                    self.spacing+=1
                    if self.spacing>10:
                        bullet=Bullet((self.rect.centerx,self.rect.bottom),"enemy")
                        GlobVar.enemyBulletList.add(bullet)
                        self.spacing=0

    def destroy(self):
        self.shot=15
                    

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(GlobVar.format_path("resources/images/aheroplane.png"))
        self.rect=self.image.get_rect()
        self.rect.center=(500,560)
        self.dx=0
        self.dy=0
        self.spacing=0

    def update(self):
        self.rect.move_ip((self.dx, self.dy))

        press=pygame.key.get_pressed()
        if press[pygame.K_SPACE]:
                self.spacing+=1
                if(self.spacing>5):
                    bullet=Bullet(self.rect.center, "player")
                    GlobVar.playerBulletList.add(bullet)
                    #shoot.play()
                    self.spacing=0
        
        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>GlobVar.width:
            self.rect.right=GlobVar.width

#Bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, _type):
        pygame.sprite.Sprite.__init__(self)
        if _type=="player":
            color=(150,200,150)
        else:
            color=(255,150,150)
        self.image=pygame.Surface([5,15])
        self.image.fill(color)
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.type=_type

    def update(self):
        if self.type=="player":
            if self.rect.bottom<0:
                self.kill()
            else:
                self.rect.y-=10
        else:
            if self.rect.top>GlobVar.height:
                self.kill()
            else:
                self.rect.y+=10


#Explosions
class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos, _type):
        pygame.sprite.Sprite.__init__(self)
        if _type=="enemy":
            self.image=pygame.image.load(GlobVar.format_path("resources/images/explosion3.png"))
        else:
            self.image=pygame.image.load(GlobVar.format_path("resources/images/explosion8.png"))
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.counter=0
        
    def update(self):
        self.counter+=1
        if self.counter>15:
            self.kill()
            

#Recieving lives
class AttainLife(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(GlobVar.format_path("resources/images/inc_life.png"))
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.counter=0
        
    def update(self):
        self.rect.y+=5
        if self.rect.y>GlobVar.height:
            self.kill()


#Lives
class Life(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(GlobVar.format_path("resources/images/shield.png"))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(GlobVar.width)
        self.rect.y=0

    def update(self):
        self.rect.y+=5
        if self.rect.bottom>GlobVar.height:
            self.kill()

