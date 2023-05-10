from random import randint 
from pygame import *
mixer.init()
font.init()
from time import time as timer

window = display.set_mode((1000, 800))
display.set_caption('Ниндзя- Фрукты')
background= transform.scale(image.load('background.png'), (1000, 800))

'''mixer.music.load('main_theme.ogg')
mixer.music.play()
cuts = mixer.Sound('fire.ogg')'''
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed, size1, size2):
        super(). __init__()
        self.image = transform.scale(image.load(image1), (size1,size2))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <595:
            self.rect.x += self.speed
        '''if keys_pressed[K_UP] and self.rect.y > 350:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed'''

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(30,650)
            self.rect.x += self.speed
            global lost          
            lost += 1

'''class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
           self.kill()'''
            
fruits = sprite.Group()

fight = True
FPS = 60
finish = False
num_f = 0
atk = 0
rei_t = False
health = 10
play_again = 1
while fight:
    for i in event.get():
        if i.type == QUIT:
            fight = False
        if i.type == KEYDOWN:
            '''if i.key == K_SPACE:
                if num_f <15:
                    shuttle.fire()
                    shots.play()
                    num_f += 1
                if num_f >= 15:
                    e = timer()
                    rei_t = True'''
            if i.key == K_ESCAPE:
                finish = True
                pause = font.SysFont('Arial', 30).render('Хотите продолжить? Нажмите R', 1 , (255, 255, 255))
                window.blit(pause, (150,250))
            if i.key == K_r:
                finish = False
                
                    
                
                
    if finish != True:
        window.blit(background, (0,0))
       
        '''touch= sprite.spritecollide(shuttle, ufos, False)
        boom =sprite.spritecollide(shuttle, astrous, True)
        get_ufos = sprite.groupcollide(ufos, bullets, True,True)
        for i in get_ufos:
            atk += 1
            ufo = Enemy('ufo.png', randint(50, 350), 0, 3, 65, 65)
            ufos.add(ufo)
        counter = font.SysFont('Arial', 30).render('Счётчик:'+ str(atk), 1 , (255, 255, 255))
        lost_t = font.SysFont('Arial',30).render('Пропущено:' + str(lost), 1 , (255, 255, 255))
        window.blit(counter, (20, 20))
        window.blit(lost_t, (50,50))'''
        if rei_t == True:
            num = timer()
            if num-e <=2:
                reshot = font.SysFont('Arial', 30).render('Wait, перезарядка...', 1 , (139, 0, 0))
                window.blit(reshot, (350, 420))
            else:
                num_f = 0
                rei_t = False
        '''if touch:
            sprite.spritecollide(shuttle, ufos, True)
            health-= 1
            ufo = Enemy('ufo.png', randint(50, 350), 0, 3, 65, 65)
            ufos.add(ufo)

            
        if health <= 0:
            finish = True
            lose = font.SysFont('Arial', 70).render('Ты проиграл!', 1 , (139, 0, 0))
            window.blit(lose, (150, 250))
        if lost >= 25:
            finish = True
            lose = font.SysFont('Arial', 70).render('Ты проиграл!', 1 , (139, 0, 0))
            window.blit(lose, (150, 250))
        if atk >= 30:
            finish = True
            win = font.SysFont('Arial', 70).render('Ты выиграл!!!', 1 , (135, 206, 250))
            window.blit(win, (150, 250))'''

    clock.tick(FPS)
    display.update()
    

display.update()