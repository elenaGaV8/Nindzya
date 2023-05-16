from random import randint 
from pygame import *
mixer.init()
font.init()
from time import time as timer

window = display.set_mode((1000, 800))
display.set_caption('Ниндзя- Фрукты')
background= transform.scale(image.load('449.jpg'), (1000, 800))

mixer.music.load('main_theme.mp3')
mixer.music.play()
'''cuts = mixer.Sound('fire.ogg')'''
'''start = mixer.Sound('начало.mp3')'''

clock = time.Clock()
lost = 0
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
        if keys_pressed[K_RIGHT] and self.rect.x <760:
            self.rect.x += self.speed
    def cut_them(self):
        self.image1 = ('ниндзя взмах.png',self.rect.centerx, self.rect.top, 8, 250, 350)
        self.image1.reset()



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 800:
            self.rect.y = 0
            self.rect.x = randint(40,900)
            global lost          
            lost += 1


nindzya = Player('ниндзя замах.png', 600, 400, 8, 350, 450)           
fruits = sprite.Group()
apple1 = Enemy('apple.png', 100, 0, 4,70,70)
apple2 = Enemy('apple.png', 800, 0, 6,70,70)

banana = Enemy('banana.png',350, 0, 2,70,70)
grapefruit = Enemy('grapefruit.png', 550, 0, 3,80,80)
kiwi1 = Enemy('kiwi.png',260, 0, 1,50,50)
kiwi2 = Enemy('kiwi.png',750, 0, 7,50,50)

watermelon = Enemy('watermelon.png',400, 0, 5,100,100)

fruits.add(apple1)
fruits.add(apple2)

fruits.add(banana)
fruits.add(grapefruit)
fruits.add(kiwi1)
fruits.add(kiwi2)

fruits.add(watermelon)
all_fruits = ['apple.png', 'banana.png', 'grapefruit.png', 'kiwi.png', 'watermelon.png']

FPS = 60
finish = False
num_f = 0
atk = 0
rei_t = False
health = 10
play_again = 1
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    text_sur = font.render(text, True, (255, 255, 255))
    text_rect = text_sur.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_sur, text_rect)


fight = True
while fight:
    for i in event.get():
        if i.type == QUIT:
            fight = False
        if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                finish = True
                pause = font.SysFont('Arial', 100).render('Pause! Нажмите R', 1 , (255, 255, 255))
                window.blit(pause, (150,250))
            if i.key == K_r:
                finish = False
            if i.key == K_f:
                nindzya = Player('ниндзя взмах.png', 600, 400, 8, 350, 450)
        elif i.type ==KEYUP:
            if i.key == K_f:
                nindzya = Player('ниндзя замах.png', nindzya.rect.x, nindzya.rect.y, 8, 350, 450)
                touch= sprite.spritecollide(nindzya, fruits, False)
                get_fruits =sprite.spritecollide(nindzya, fruits, True)
                for i in get_fruits:
                    atk += 1
                    fruit = Enemy(all_fruits[randint(0, 4)], randint(50, 950), 0, randint(1, 6), randint(50, 100),randint(50, 100))
                    fruits.add(fruit)

                
                    
                
    
    if finish != True:

        window.blit(background, (0,0))
        fruits.draw(window)
        fruits.update()
        nindzya.reset()
        nindzya.update()            
            
        counter = font.SysFont('Arial', 40).render('Счётчик:'+ str(atk), 1 , (255, 255, 255))
        lost_t = font.SysFont('Arial',40).render('Пропущено:' + str(lost), 1 , (255, 255, 255))
        
        window.blit(counter, (20, 20))
        window.blit(lost_t, (50,50))
        
        if lost >= 25:
            finish = True
            lose = font.SysFont('Arial', 100).render('Ты проиграл!', 1 , (139, 0, 0))
            window.blit(lose, (150, 250))
        if atk >= 40:
            finish = True
            win = font.SysFont('Arial', 100).render('Ты выиграл!!!', 1 , (135, 206, 250))
            window.blit(win, (150, 250))


    clock.tick(FPS)
    display.update()

display.update()
