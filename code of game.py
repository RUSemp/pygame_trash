import pygame

class Animation:
    def __init__ (self, sprites=None, time=100):
        self.sprites = sprites
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

    def update(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites):
                self.frame = 0

    def get_sprite(self):        
        return self.sprites[self.frame]

class Shooting:
    def __init__(self,x,y,d_stand, Bow):
        self.x=x
        self.y=y
        self.d_stand=d_stand
        if d_stand==1 or d_stand==2:
            self.speed = 10
        else:
            self.speed = -10
        self.Bow=Bow
    def draw(self):
        screen.blit(self.Bow, (self.x,self.y))

class Target:
    def __init__(self, Left, Right, Front, Back, WalkLeft, WalkRight, WalkFront, WalkBack, AtackLeft, AtackRight, AtackFront, AtackBack, xm,ym, m_direct):
        self.Left=Left
        self.Right=Right
        self.Front=Front
        self.Back=Back
        self.WalkLeft=WalkLeft
        self.WalkRight=WalkRight
        self.WalkFront=WalkFront
        self.WalkBack=WalkBack
        self.AtackLeft=AtackLeft
        self.AtackRight=AtackRight
        self.AtackFront=AtackFront
        self.AtackBack=AtackBack
        self.m_direct=m_direct
        self.dt=dt
        self.xm=xm
        self.ym=ym
        self.speed=5
        self.health=100
    def StandLeft(self):
        screen.blit(self.Left, (self.xm,self.ym))

    def StandRight(self):
        screen.blit(self.Right, (self.xm,self.ym))

    def StandFront(self):
        screen.blit(self.Front, (self.xm,self.ym))

    def StandBack(self):
        screen.blit(self.Back, (self.xm,self.ym))

    def Walking(self,dt):
        if self.m_direct==1:
            self.WalkFront.update(dt)
            screen.blit(self.WalkFront.get_sprite(), (self.xm,self.ym))
        if self.m_direct==-1:
            self.WalkBack.update(dt)
            screen.blit(self.WalkBack.get_sprite(), (self.xm,self.ym))
        if self.m_direct==2:
            self.WalkRight.update(dt)
            screen.blit(self.WalkRight.get_sprite(), (self.xm,self.ym))
        if self.m_direct==-2:
            self.WalkLeft.update(dt)
            screen.blit(self.WalkLeft.get_sprite(), (self.xm,self.ym))

    def TargetLeft(self):
        self.AtackLeft.update(self.dt)
        screen.blit(self.AtackLeft.get_sprite(), (self.xm,self.ym))
        
    def TargetRight(self):
        self.AtackRight.update(self.dt)
        screen.blit(self.AtackRight.get_sprite(), (self.xm,self.ym))
        
    def TargetFront(self,dt):
        self.AtackFront.update(dt)
        screen.blit(self.AtackFront.get_sprite(), (self.xm,self.ym))
        
    def TargetBack(self):
        self.AtackBack.update(self.dt)
        screen.blit(self.AtackBack.get_sprite(), (self.xm,self.ym))
    

pygame.init()

display_width = 960
display_height = 720

time = 50

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (7,74,7)
bright_red = (255,0,0)
bright_green = (0,255,0)


walk =[pygame.image.load('Огр вперёд'+str(i)+'.png') for i in range(2,10)]
left = [pygame.image.load('Огр влево'+str(i)+'.png') for i in range(1,10)]
back = [pygame.image.load('Огр назад'+str(i)+'.png') for i in range(2,10)]
right = [pygame.image.load('Огр вправо'+str(i)+'.png') for i in range(1,10)]
Orc_anything_front = [pygame.image.load('Огр что-то вперёд'+str(i)+'.png') for i in range(1,8)]
Orc_anything_left = [pygame.image.load('Огр что-то влево'+str(i)+'.png') for i in range(1,8)]
Orc_anything_right = [pygame.image.load('Огр что-то вправо'+str(i)+'.png') for i in range(1,8)]
Orc_anything_back = [pygame.image.load('Огр что-то назад'+str(i)+'.png') for i in range(1,8)]
Elsa_front = [pygame.image.load('Эльза вперёд'+str(i)+'.png') for i in range(2,10)]
Elsa_left = [pygame.image.load('Эльза влево'+str(i)+'.png') for i in range(1,10)]
Elsa_right = [pygame.image.load('Эльза вправо'+str(i)+'.png') for i in range(1,10)]
Elsa_back = [pygame.image.load('Эльза назад'+str(i)+'.png') for i in range(2,10)]
Elsa_free_front = [pygame.image.load('Эльза повседнев вперёд'+str(i)+'.png') for i in range(2,10)]
Elsa_free_left = [pygame.image.load('Эльза повседнев влево'+str(i)+'.png') for i in range(1,10)]
Elsa_free_right = [pygame.image.load('Эльза повседнев вправо'+str(i)+'.png') for i in range(1,10)]
Elsa_free_back = [pygame.image.load('Эльза повседнев назад'+str(i)+'.png') for i in range(2,10)]
shoot_front = [pygame.image.load('Эльза стрельба вперёд'+str(i)+'.png') for i in range(1,14)]
shoot_left = [pygame.image.load('Эльза стрельба влево'+str(i)+'.png') for i in range(1,14)]
shoot_right = [pygame.image.load('Эльза стрельба вправо'+str(i)+'.png') for i in range(1,14)]
shoot_back = [pygame.image.load('Эльза стрельба назад'+str(i)+'.png') for i in range(1,14)]
shoot_free_front = [pygame.image.load('Эльза повседнев стрельба вперёд'+str(i)+'.png') for i in range(1,14)]
shoot_free_left = [pygame.image.load('Эльза повседнев стрельба влево'+str(i)+'.png') for i in range(1,14)]
shoot_free_right = [pygame.image.load('Эльза повседнев стрельба вправо'+str(i)+'.png') for i in range(1,14)]
shoot_free_back = [pygame.image.load('Эльза повседнев стрельба назад'+str(i)+'.png') for i in range(1,14)]
Lysyk_front = [pygame.image.load('Лысик прямо'+str(i)+'.png') for i in range(2,10)]
Lysyk_left = [pygame.image.load('Лысик влево'+str(i)+'.png') for i in range(1,10)]
Lysyk_right = [pygame.image.load('Лысик вправо'+str(i)+'.png') for i in range(1,10)]
Lysyk_back = [pygame.image.load('Лысик назад'+str(i)+'.png') for i in range(2,10)]
Lysyk_thrust_front = [pygame.image.load('Лысик удар'+str(i)+'.png') for i in range(1,9)]
Lysyk_thrust_left = [pygame.image.load('Лысик удар влево'+str(i)+'.png') for i in range(1,9)]
Lysyk_thrust_right = [pygame.image.load('Лысик удар вправо'+str(i)+'.png') for i in range(1,9)]
Lysyk_thrust_back = [pygame.image.load('Лысик удар назад'+str(i)+'.png') for i in range(1,9)]
Skelet_front = [pygame.image.load('Скелет вперёд'+str(i)+'.png') for i in range(2,10)]
Skelet_left = [pygame.image.load('Скелет влево'+str(i)+'.png') for i in range(1,10)]
Skelet_right = [pygame.image.load('Скелет вправо'+str(i)+'.png') for i in range(1,10)]
Skelet_back = [pygame.image.load('Скелет назад'+str(i)+'.png') for i in range(2,10)]
Skelet_slash_front = [pygame.image.load('Скелет удар вперёд'+str(i)+'.png') for i in range(1,7)]
Skelet_slash_left = [pygame.image.load('Скелет удар влево'+str(i)+'.png') for i in range(1,7)]
Skelet_slash_right = [pygame.image.load('Скелет удар вправо'+str(i)+'.png') for i in range(1,7)]
Skelet_slash_back = [pygame.image.load('Скелет удар назад'+str(i)+'.png') for i in range(1,7)]

Walking_Orc = Animation(walk, time)
Walk_Left_Orc = Animation(left, time)
Walk_Back_Orc = Animation(back, time)
Walk_Right_Orc = Animation(right, time)
Walk_Front_Elsa = Animation(Elsa_front, time)
Walk_Left_Elsa = Animation(Elsa_left, time)
Walk_Right_Elsa = Animation(Elsa_right, time)
Walk_Back_Elsa = Animation(Elsa_back, time)
Walk_Free_Front_Elsa = Animation(Elsa_free_front, time)
Walk_Free_Left_Elsa = Animation(Elsa_free_left, time)
Walk_Free_Right_Elsa = Animation(Elsa_free_right, time)
Walk_Free_Back_Elsa = Animation(Elsa_free_back, time)
Walk_Front_Lysyk = Animation(Lysyk_front, time)
Walk_Left_Lysyk = Animation(Lysyk_left, time)
Walk_Right_Lysyk = Animation(Lysyk_right, time)
Walk_Back_Lysyk = Animation(Lysyk_back, time)
Walk_Front_Skelet = Animation(Skelet_front, time)
Walk_Left_Skelet = Animation(Skelet_left, time)
Walk_Right_Skelet = Animation(Skelet_right, time)
Walk_Back_Skelet = Animation(Skelet_back, time)

Anythink_Front_Orc = Animation(Orc_anything_front, time+25)
Anythink_Left_Orc = Animation(Orc_anything_left, time+25)
Anythink_Right_Orc = Animation(Orc_anything_right, time+25)
Anythink_Back_Orc = Animation(Orc_anything_back, time+25)
Shoot_Front_Elsa = Animation(shoot_front, time)
Shoot_Left_Elsa = Animation(shoot_left, time)
Shoot_Right_Elsa = Animation(shoot_right, time)
Shoot_Back_Elsa = Animation(shoot_back, time)
Shoot_Free_Front_Elsa = Animation(shoot_free_front, time)
Shoot_Free_Left_Elsa = Animation(shoot_free_left, time)
Shoot_Free_Right_Elsa = Animation(shoot_free_right, time)
Shoot_Free_Back_Elsa = Animation(shoot_free_back, time)
Thrust_Front_Lysyk = Animation(Lysyk_thrust_front, time)
Thrust_Left_Lysyk = Animation(Lysyk_thrust_left, time)
Thrust_Right_Lysyk = Animation(Lysyk_thrust_right, time)
Thrust_Back_Lysyk = Animation(Lysyk_thrust_back, time)
Slash_Front_Skelet = Animation(Skelet_slash_front, time)
Slash_Left_Skelet = Animation(Skelet_slash_left, time)
Slash_Right_Skelet = Animation(Skelet_slash_right, time)
Slash_Back_Skelet = Animation(Skelet_slash_back, time)

gameDisplay = pygame.display.set_mode((display_width,display_height))
screen = pygame.Surface((display_width,display_height))
pygame.display.set_caption('Тип выход из этой игры')

Orc_front = pygame.image.load('Огр вперёд1.png')
Orc_left = pygame.image.load('Огр влево1.png')
Orc_right = pygame.image.load('Огр вправо1.png')
Orc_back = pygame.image.load('Огр назад1.png')
Elsa_stand_front = pygame.image.load('Эльза вперёд1.png')
Elsa_stand_left = pygame.image.load('Эльза влево1.png')
Elsa_stand_right = pygame.image.load('Эльза вправо1.png')
Elsa_stand_back = pygame.image.load('Эльза назад1.png')
Elsa_free_stand_front = pygame.image.load('Эльза повседнев вперёд1.png')
Elsa_free_stand_left = pygame.image.load('Эльза повседнев влево1.png')
Elsa_free_stand_right = pygame.image.load('Эльза повседнев вправо1.png')
Elsa_free_stand_back = pygame.image.load('Эльза повседнев назад1.png')
Lysyk_stand_front = pygame.image.load('Лысик прямо1.png')
Lysyk_stand_left = pygame.image.load('Лысик влево1.png')
Lysyk_stand_right = pygame.image.load('Лысик вправо1.png')
Lysyk_stand_back = pygame.image.load('Лысик назад1.png')
Skelet_stand_front = pygame.image.load('Скелет вперёд1.png')
Skelet_stand_left = pygame.image.load('Скелет влево1.png')
Skelet_stand_right = pygame.image.load('Скелет вправо1.png')
Skelet_stand_back = pygame.image.load('Скелет назад1.png')

Lok1 = pygame.image.load('Побережье.png')
Lok2_1 = pygame.image.load('Бар на берегу.png')
Lok2_2 = pygame.image.load('Бар на берегу2.png')
Lok3 = pygame.image.load('Каюта.png')
Lok4_1 = pygame.image.load('Корридор1.png')
Lok4_2 = pygame.image.load('Корридор2.png')
Lok5 = pygame.image.load('Бар на корабле.png')
Lok6 = pygame.image.load('казино на корабле.png')
Lok8_1 = pygame.image.load('Комната в замке.png')
Lok8_2 = pygame.image.load('Комната в замке2.png')
Lok11_1 = pygame.image.load('корридор замка1.png')
Lok11_2 = pygame.image.load('корридор замка2.png')
Lok11_3 = pygame.image.load('корридор замка3.png')
Lok11_4 = pygame.image.load('корридор замка4.png')
Lok12 = pygame.image.load('Главный зал.png')
Lok13_1 = pygame.image.load('кровавая вечеринка.png')
Lok13_2 = pygame.image.load('кровавая вечеринка2.png')

Arrow_Left = pygame.image.load('стрела1 влево.png')
Arrow_Right = pygame.image.load('Стрела вправо.png')
Arrow_Up = pygame.image.load('Стрела вверх.png')
Arrow_Down = pygame.image.load('Стрела вниз.png')

DEAD_END = pygame.image.load('DEAD END.png')
Chat = pygame.image.load('текстовая рамка.png')

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action = None):
    mouce = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouce[0] > x and y + h > mouce[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects(msg,smallText, black)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def DEADEND():
    screen.blit(DEAD_END, (0,0))
    button('Я смогу лучше', 150,500,250,50,green,bright_green,LOK1)
    button('Это невозможно ', 550,500,250,50,red,bright_red,quitgame)

def message_display(text,x,y):
    LargeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, LargeText, white)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def CHAT1():
    screen.blit(Chat, (0,0))
    message_display('Не хотите остановиться в моём замке на время вашего отпуска?',(display_width/2),550)
    message_display('Добираться мы до него будем на моём личной лайнере',(display_width/2),600)
    button('Да, хочу', 150,650,100,50,green,bright_green,LOK3)
    button('Нет, спасибо', 550,650,100,50,red,bright_red,WIN)

def CHAT2():
    screen.blit(Chat,(0,0))
    message_display('-Вы',60,500)
    message_display('Девчёнки, Что-то странное твориться на этом лайнере...',(display_width/2),550)
    message_display('На меня только что напал скелет в кафетерии!',(display_width/2),600)
    message_display('-Блондинка: Странно... Мы никого там не видели...',(display_width/2),650)
    button('Пропустить 4 дня',710,670,250,50,red,bright_red,LOK8)

def CHAT3():
    screen.blit(Chat,(0,0))
    message_display('Пожалуйста помоги! Я проснулся, а постояльцы пропали!',(display_width/2),550)
    message_display('По всему замку одни монстры шастают,',(display_width/2),600)
    message_display('Теперь даже выйти из комнаты не могу',(display_width/2),650)
    button('Перебить всех монстров',610,670,300,50,red,bright_red,LOK11_1)

def CHAT4():
        screen.blit(Chat,(0,0))
        message_display('Браво браво, ты всё же дошла до моей ловушки!',(display_width/2),550)
        message_display('Ты настолько наивна что это даже смешно!',(display_width/2),600)
        message_display('!!!ВЗЯТЬ ЕЁ!!!',(display_width/2),650)
        button('Продолжить',610,670,300,50,red,bright_red,Final)

def WIN():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        screen.fill(black)

        message_display('Логично же предположить,',(display_width/2),(display_height/2))
        message_display('Что останавливаться у незнакомца в замке плохая идея!',(display_width/2),(display_height/2)+60)
        message_display('ВЫ ВЫЙГРАЛИ! (ну точнее хотя бы выжили',(display_width/2),(display_height/2)+120)
        gameDisplay.blit(screen,(0,0)) 
        pygame.display.flip()
        dt=clock.tick(40)




def lok1():
    screen.blit(Lok1, (0,0))


def WalkFrontElsa(dt,x,y):
    Walk_Front_Elsa.update(dt)
    screen.blit(Walk_Front_Elsa.get_sprite(), (x,y))

def WalkLeftElsa(dt,x,y):
    Walk_Left_Elsa.update(dt)
    screen.blit(Walk_Left_Elsa.get_sprite(), (x,y))

def WalkRightElsa(dt,x,y):
    Walk_Right_Elsa.update(dt)
    screen.blit(Walk_Right_Elsa.get_sprite(), (x,y))

def WalkBackElsa(dt,x,y):
    Walk_Back_Elsa.update(dt)
    screen.blit(Walk_Back_Elsa.get_sprite(), (x,y))

def ShootFrontElsa(dt,x,y):
    Shoot_Front_Elsa.update(dt)
    screen.blit(Shoot_Front_Elsa.get_sprite(),(x,y))

def ShootLeftElsa(dt,x,y):
    Shoot_Left_Elsa.update(dt)
    screen.blit(Shoot_Left_Elsa.get_sprite(), (x,y))

def ShootRightElsa(dt,x,y):
    Shoot_Right_Elsa.update(dt)
    screen.blit(Shoot_Right_Elsa.get_sprite(), (x,y))

def ShootBackElsa(dt,x,y):
    Shoot_Back_Elsa.update(dt)
    screen.blit(Shoot_Back_Elsa.get_sprite(), (x,y))

def WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand, f_shooting):
    if y_change>0:
        WalkFrontElsa(dt,x,y)
    elif y_change<0:
        WalkBackElsa(dt,x,y)
    elif x_change>0:
        WalkRightElsa(dt,x,y)
    elif x_change<0:
        WalkLeftElsa(dt,x,y)
    else:
        if d_stand == 2:
            if f_shooting == 2:
                ShootFrontElsa(dt,x,y)
            elif f_shooting ==0:
                screen.blit(Elsa_stand_front, (x,y))
        elif d_stand == -2:
            if f_shooting == -2:
                ShootBackElsa(dt,x,y)
            elif f_shooting == 0:
                screen.blit(Elsa_stand_back, (x,y))
        elif d_stand == 1:
            if f_shooting == 1:
                ShootRightElsa(dt,x,y)
            elif f_shooting == 0:
                screen.blit(Elsa_stand_right, (x,y))
        elif d_stand == -1:
            if f_shooting == -1:
                ShootLeftElsa(dt,x,y)
            elif f_shooting == 0:
                screen.blit(Elsa_stand_left, (x,y))
        



def WalkFreeFrontElsa(dt,x,y):
    Walk_Free_Front_Elsa.update(dt)
    screen.blit(Walk_Free_Front_Elsa.get_sprite(), (x,y))

def WalkFreeLeftElsa(dt,x,y):
    Walk_Free_Left_Elsa.update(dt)
    screen.blit(Walk_Free_Left_Elsa.get_sprite(), (x,y))

def WalkFreeRightElsa(dt,x,y):
    Walk_Free_Right_Elsa.update(dt)
    screen.blit(Walk_Free_Right_Elsa.get_sprite(), (x,y))

def WalkFreeBackElsa(dt,x,y):
    Walk_Free_Back_Elsa.update(dt)
    screen.blit(Walk_Free_Back_Elsa.get_sprite(), (x,y))

def ShootFreeFrontElsa(dt,x,y):
    Shoot_Free_Front_Elsa.update(dt)
    screen.blit(Shoot_Free_Front_Elsa.get_sprite(),(x,y))

def ShootFreeLeftElsa(dt,x,y):
    Shoot_Free_Left_Elsa.update(dt)
    screen.blit(Shoot_Free_Left_Elsa.get_sprite(), (x,y))

def ShootFreeRightElsa(dt,x,y):
    Shoot_Free_Right_Elsa.update(dt)
    screen.blit(Shoot_Free_Right_Elsa.get_sprite(), (x,y))

def ShootFreeBackElsa(dt,x,y):
    Shoot_Free_Back_Elsa.update(dt)
    screen.blit(Shoot_Free_Back_Elsa.get_sprite(), (x,y))

def WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand, f_shooting):
    if y_change>0:
        WalkFreeFrontElsa(dt,x,y)
    elif y_change<0:
        WalkFreeBackElsa(dt,x,y)
    elif x_change>0:
        WalkFreeRightElsa(dt,x,y)
    elif x_change<0:
        WalkFreeLeftElsa(dt,x,y)
    else:
        if d_stand == 2:
            if f_shooting == 2:
                ShootFreeFrontElsa(dt,x,y,)
            elif f_shooting ==0:
                screen.blit(Elsa_free_stand_front, (x,y))
        elif d_stand == -2:
            if f_shooting == -2:
                ShootFreeBackElsa(dt,x,y)
            elif f_shooting == 0:
                screen.blit(Elsa_free_stand_back, (x,y))
        elif d_stand == 1:
            if f_shooting == 1:
                ShootFreeRightElsa(dt,x,y)
            elif f_shooting == 0:
                screen.blit(Elsa_free_stand_right, (x,y))
        elif d_stand == -1:
            if f_shooting == -1:
                ShootFreeLeftElsa(dt,x,y)
            elif f_shooting == 0:
                screen.blit(Elsa_free_stand_left, (x,y))

clock = pygame.time.Clock()
dt = 0

x = (display_width * 0.3)
y = (display_height * 0.3)
x_change = 0
y_change = 0
d_stand = 2
f_shooting = 0
Arrows=[]
Targets=[]


def LOK1():
    Targets=[]
    x = 650
    y = 0
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    Targets.append(Target(Orc_left, Orc_right, Orc_front, Orc_back, Walk_Left_Orc, Walk_Right_Orc, Walking_Orc, Walk_Back_Orc, Anythink_Left_Orc, Anythink_Right_Orc, Anythink_Front_Orc, Anythink_Back_Orc, xm,ym, m_direct))

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x<=615 and y<=390 and x>=410 or x<=200 and x >=150 and y<=390 or x<=75 and x>=23 and y<=390 or x<=0:
                        x_change = 0
                    else:
                        x_change = -5
                        d_stand = -1
             
                if event.key == pygame.K_RIGHT:
                    if x>=400 and y<=390 and x<=613 or x>=143 and x<=198 and y<=390 or x>=20 and x<=73 and y<=390 or x>=710:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
                if event.key == pygame.K_UP:
                    if y<=0 or y<=391 and x>=400 and x<=613 or y<=366 and x>=200 and x<=400 or y<=391 and x>=143 and x<=200 or y<=296 and x<=143 and x>=73 or y<=391 and x>=20 and x<=73 or y<=366 and x<=20:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2
                
                if event.key == pygame.K_DOWN:
                    if y>=466:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

                
                        
                if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
        
        x+=x_change
        y+=y_change

        
        lok1()

        if x<=615 and y<=390 and x>=410 or x<=200 and x >=150 and y<=390 or x<=75 and x>=23 and y<=390 or x<=0:
                        x_change = 0
        if x>=400 and y<=390 and x<=613 or x>=143 and x <=198 and y<=390 or x>=20 and x<=73 and y<=390 or x>=710:
                        x_change=0
        if y<=0 or y<=391 and x>=400 and x<=613 or y<=366 and x>=200 and x<=400 or y<=391 and x>=143 and x<=200 or y<=296 and x<=143 and x>=73 or y<=391 and x>=20 and x<=73 or y<=366 and x<=20:
                        y_change=0
        if y>=466:
            y_change=0

        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()

        print(Health)
                    

        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if 73<x<143 and y==295:
            LOK2()
            quitgame()

        if Health<=0:
            DEADEND()

        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK2():
    x = 30
    y = 370
    x_change = 0
    y_change = 0
    d_stand = 2
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok2_1,(0,0))

        if x!=710:
            x_change=5
        elif x==710:
            x_change=0
        if y!=350:
            y_change=-5
        elif y==350:
            y_change=0


        d_stand=-2

        if x == 710 and y == 350:
            screen.blit(Lok2_2, (0,0))
            CHAT1()

        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK3():
    x = 510
    y = 210
    x_change = 0
    y_change = 0
    d_stand = 2
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==200 or x==365 and y<195 or x==240 and 220<y<395 or x==435 and y>520 or 270<x<=430 and 235<y<380:
                        x_change=0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                   if x==685 or x==520 and y<250 or x==645 and 260<y<430 or x==600 and 330<y<395 or x==455 and y>520 or 270<=x<430 and 235<y<380 or x==280 and y<195:
                       x_change = 0
                   else:
                       x_change = 5
                       d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==160 or y==195 and 280<x<365 or y==250 and x>520 or y==380 and 270<x<420 or y==395 and 600<x or y==430 and x>645 or y==395 and x<240 :
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==570 or y==330 and x>600 or y==235 and 270<x<380 or y==260 and x>645 or y==220 and x<240 or y==520 and 455<x or y==520 and x<435:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                    elif d_stand == -2:
                       f_shooting = -2
                    elif d_stand == 1:
                        f_shooting = 1
                    elif d_stand == -1:
                        f_shooting = -1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok3,(0,0))

        if x==200 or x==365 and y<195 or x==240 and 220<y<395 or x==435 and y>520 or 270<x<=430 and 235<y<380:
                        x_change=0

        if x==685 or x==520 and y<250 or x==645 and 260<y<430 or x==600 and 330<y<395 or x==455 and y>520 or 270<=x<430 and 235<y<380 or x==280 and y<195:
                       x_change = 0

        if y==160 or y==195 and 280<x<365 or y==250 and x>520 or y==380 and 270<x<420 or y==395 and 600<x or y==430 and x>645 or y==395 and x<240 :
                        y_change=0

        if y==570 or y==330 and x>600 or y==235 and 270<x<380 or y==260 and x>645 or y==220 and x<240 or y==520 and 455<x or y==520 and x<435:
                        y_change=0

        if 435<x<455 and y==570:
            LOK4_1()
            crashed=True
        
        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK4_1():
    x = 610
    y = 175
    x_change = 0
    y_change = 0
    d_stand = 2
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==74 or x==605 and y<205:
                        x_change=0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==935 or x==620 and y<205:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==160 or y==205 and x<605 or y==205 and x>620:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==330:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                    elif d_stand == -2:
                       f_shooting = -2
                    elif d_stand == 1:
                        f_shooting = 1
                    elif d_stand == -1:
                        f_shooting = -1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok4_1,(0,0))

        if x==74 or x==605 and y<205:
                        x_change=0

        if x==935 or x==620 and y<205:
                        x_change=0

        if y==160 or y==205 and x<605 or y==205 and x>620:
                        y_change=0

        if y==330:
                        y_change=0

        if x==935 and 205<y<330:
            LOK4_2()
            crashed=True
        
        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK4_2():
    x = 10
    y = 290
    x_change = 0
    y_change = 0
    d_stand = 2
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==0:
                        x_change=0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==790 or x==740 and y<250 or x==740 and y>280:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==205 or y==250 and x>740:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==330 or y==280 and x>740:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                    elif d_stand == -2:
                       f_shooting = -2
                    elif d_stand == 1:
                        f_shooting = 1
                    elif d_stand == -1:
                        f_shooting = -1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok4_2,(0,0))

        if x==0:
                        x_change=0

        if x==790 or x==740 and y<250 or x==740 and y>280:
                        x_change=0

        if y==205 or y==250 and x>740:
                        y_change=0

        if y==330 or y==280 and x>740:
                        y_change=0

        if x==790 and 250<y<280:
            LOK5()
            crashed=True

        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK5():
    Targets=[]
    x = 160
    y = 320
    xm=390
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,xm,ym,m_direct))
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==145 or x==190 and y<300 or x==190 and y>330 or x==340 and y>380 or x==575 and 205<y<400 or x==575 and y>445 or x==740 and y<155 or x==815 and 205<y<400 or x==815 and y>480:
                        x_change=0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==835 or x==815 and y<155 or x==645 and 205<y<400 or x==645 and y>480 or x==400 and 205<y<400 or x==400 and y>445:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                    
               if event.key == pygame.K_UP:
                    if y==0 or y==155 and x<740 or y==155 and x>815 or y==300 and x<190 or y==400 and 400<x<575 or y==400 and 645<x<815:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==615 or y==480 and 645<x<815 or y==445 and 400<x<575 or y==380 and x<340 or y==330 and x<190 or y==205 and 400<x<575 or y==205 and 645<x<815:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok5,(0,0))

        if x==145 or x==190 and y<300 or x==190 and y>330 or x==340 and y>380 or x==575 and 205<y<400 or x==575 and y>445 or x==740 and y<155 or x==815 and 205<y<400 or x==815 and y>480:
                        x_change=0

        if x==835 or x==815 and y<155 or x==645 and 205<y<400 or x==645 and y>480 or x==400 and 205<y<400 or x==400 and y>445:
                        x_change=0

        if y==0 or y==155 and x<740 or y==155 and x>815 or y==300 and x<190 or y==400 and 400<x<575 or y==400 and 645<x<815:
                        y_change=0

        if y==615 or y==480 and 645<x<815 or y==445 and 400<x<575 or y==380 and x<340 or y==330 and x<190 or y==205 and 400<x<575 or y==205 and 645<x<815:
                        y_change=0

        if 740<x<815 and y==0:
            LOK6()

        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()

        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if Health<=0:
            DEADEND()
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK6():
    x = 760
    y = 165
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok6,(0,0))

        if y!=300:
            y_change=5
        elif x!=470:
            x_change=-5
        if y==300:
            y_change=0
        if x==470:
            x_change=0

        if x==470 and y==300:
            CHAT2()
        

        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK8():
    x = 420
    y = 505
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok8_1,(0,0))

        if x!=470:
            x_change=5
        else:
            x_change=0
        if y!=350:
            y_change=-5
        else:
            y_change=0

        if x==470 and y ==350:
            CHAT3()
        d_stand=-2

        WalkingOrShootingFreeElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK11_1():
    Targets=[]
    x = 170
    y = 235
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    Targets.append(Target(Lysyk_stand_left, Lysyk_stand_right, Lysyk_stand_front, Lysyk_stand_back, Walk_Left_Lysyk, Walk_Right_Lysyk, Walk_Front_Lysyk, Walk_Back_Lysyk, Thrust_Left_Lysyk, Thrust_Right_Lysyk, Thrust_Front_Lysyk, Thrust_Back_Lysyk,710,225,m_direct))
    Targets.append(Target(Lysyk_stand_left, Lysyk_stand_right, Lysyk_stand_front, Lysyk_stand_back, Walk_Left_Lysyk, Walk_Right_Lysyk, Walk_Front_Lysyk, Walk_Back_Lysyk, Thrust_Left_Lysyk, Thrust_Right_Lysyk, Thrust_Front_Lysyk, Thrust_Back_Lysyk,845,165,m_direct))
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,515,190,m_direct))
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,575,260,m_direct))
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==160:
                        x_change=0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==930:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==155:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==280:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok11_1,(0,0))

        if x==160:
                        x_change=0

        if x==930:
                        x_change=0

        if y==155:
                        y_change=0

        if y==280:
                        y_change=0

        if x==930 and 155<y<280:
            LOK11_2()

        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()
        

        WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if Health<=0:
            DEADEND()
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK11_2():
    Targets=[]
    x = 10
    y = 235
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    Targets.append(Target(Lysyk_stand_left, Lysyk_stand_right, Lysyk_stand_front, Lysyk_stand_back, Walk_Left_Lysyk, Walk_Right_Lysyk, Walk_Front_Lysyk, Walk_Back_Lysyk, Thrust_Left_Lysyk, Thrust_Right_Lysyk, Thrust_Front_Lysyk, Thrust_Back_Lysyk,710,225,m_direct))
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,575,260,m_direct))
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==0 or x==625 and y>280:
                        x_change=0 
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==785:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==155:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==645 or y==280 and x<625:
                        y_change=0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok11_2,(0,0))

        if x==0 or x==625 and y>280:
                        x_change=0 

        if x==785:
                        x_change=0

        if y==155:
                        y_change=0

        if y==645 or y==280 and x<625:
                        y_change=0

        if y==645 and 625<x<785:
            LOK11_3()

        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()
        

        WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if Health<=0:
            DEADEND()
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK11_3():
    Targets=[]
    x = 400
    y = 10
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    Targets.append(Target(Orc_left, Orc_right, Orc_front, Orc_back, Walk_Left_Orc, Walk_Right_Orc, Walking_Orc, Walk_Back_Orc, Anythink_Left_Orc, Anythink_Right_Orc, Anythink_Front_Orc, Anythink_Back_Orc, 400,400, m_direct))
    Targets.append(Target(Orc_left, Orc_right, Orc_front, Orc_back, Walk_Left_Orc, Walk_Right_Orc, Walking_Orc, Walk_Back_Orc, Anythink_Left_Orc, Anythink_Right_Orc, Anythink_Front_Orc, Anythink_Back_Orc, 480,400, m_direct))
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,440,500,m_direct))
    Targets.append(Target(Lysyk_stand_left, Lysyk_stand_right, Lysyk_stand_front, Lysyk_stand_back, Walk_Left_Lysyk, Walk_Right_Lysyk, Walk_Front_Lysyk, Walk_Back_Lysyk, Thrust_Left_Lysyk, Thrust_Right_Lysyk, Thrust_Front_Lysyk, Thrust_Back_Lysyk,440,600,m_direct))

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==360:
                        x_change = 0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==520:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==0:
                        y_change=0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==645:
                        y_change =0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok11_3,(0,0))

        if x==360:
                        x_change = 0

        if x==520:
                        x_change=0

        if y==0:
                        y_change=0

        if y==645:
                        y_change =0

        if y==645 and 360<x<520:
            LOK11_4()


        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()
        

        WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if Health<=0:
            DEADEND()
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK11_4():
    Targets=[]
    x = 700
    y = 10
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x == 0 or x==625 and y<250:
                        x_change = 0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x == 785:
                        x_change = 0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==0 or y==520 and x<625:
                        y_change = 0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==380:
                        y_change =0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok11_4,(0,0))

        if x == 0 or x==625 and y<250:
                        x_change = 0

        if x == 785:
                        x_change = 0

        if y==0 or y==520 and x<625:
                        y_change = 0

        if y==380:
                        y_change =0

        if x==0 and 250<y<380:
            LOK12()


        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()
        

        WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if Health<=0:
            DEADEND()
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK12():
    Targets=[]
    x = 905
    y = 465
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    Hero_health=100
    h_damage=3
    Health=100
    Targets.append(Target(Lysyk_stand_left, Lysyk_stand_right, Lysyk_stand_front, Lysyk_stand_back, Walk_Left_Lysyk, Walk_Right_Lysyk, Walk_Front_Lysyk, Walk_Back_Lysyk, Thrust_Left_Lysyk, Thrust_Right_Lysyk, Thrust_Front_Lysyk, Thrust_Back_Lysyk,700,200,m_direct))
    Targets.append(Target(Lysyk_stand_left, Lysyk_stand_right, Lysyk_stand_front, Lysyk_stand_back, Walk_Left_Lysyk, Walk_Right_Lysyk, Walk_Front_Lysyk, Walk_Back_Lysyk, Thrust_Left_Lysyk, Thrust_Right_Lysyk, Thrust_Front_Lysyk, Thrust_Back_Lysyk,700,600,m_direct))
    Targets.append(Target(Orc_left, Orc_right, Orc_front, Orc_back, Walk_Left_Orc, Walk_Right_Orc, Walking_Orc, Walk_Back_Orc, Anythink_Left_Orc, Anythink_Right_Orc, Anythink_Front_Orc, Anythink_Back_Orc, 450,200, m_direct))
    Targets.append(Target(Orc_left, Orc_right, Orc_front, Orc_back, Walk_Left_Orc, Walk_Right_Orc, Walking_Orc, Walk_Back_Orc, Anythink_Left_Orc, Anythink_Right_Orc, Anythink_Front_Orc, Anythink_Back_Orc, 450,600, m_direct))
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,180,200,m_direct))
    Targets.append(Target(Skelet_stand_left,Skelet_stand_right,Skelet_stand_front,Skelet_stand_back,Walk_Left_Skelet,Walk_Right_Skelet,Walk_Front_Skelet,Walk_Back_Skelet,Slash_Left_Skelet,Slash_Right_Skelet,Slash_Front_Skelet,Slash_Back_Skelet,180,600,m_direct))

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if x==20 or x==380 and y<225 or x==670 and y<225 or x== 745 and 250<y<540:
                        x_change=0
                    else:
                        x_change = -5
                        d_stand = -1
                
               if event.key == pygame.K_RIGHT:
                    if x==905 or x==545 and y<225 or x==255 and y<225 or x==180 and 250<y<540:
                        x_change=0
                    else:
                        x_change = 5
                        d_stand = 1
                
               if event.key == pygame.K_UP:
                    if y==155 or y==225 and 255<x<380 or y==225 and 545<x<670 or y==540 and 180<x<745:
                        y_change = 0
                    else:
                        y_change = -5
                        d_stand = -2

               if event.key == pygame.K_DOWN:
                    if y==645 or y==250 and 180<x<745:
                        y_change =0
                    else:
                        y_change = 5
                        d_stand = 2

               if event.key == pygame.K_SPACE:
                    if d_stand == 2:
                        f_shooting = 2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Down))
                    elif d_stand == -2:
                        f_shooting = -2
                        Arrows.append(Shooting(x+10,y,d_stand,Arrow_Up))
                    elif d_stand == 1:
                        f_shooting = 1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Right))
                    elif d_stand == -1:
                        f_shooting = -1
                        Arrows.append(Shooting(x,y+20,d_stand,Arrow_Left))
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok12,(0,0))

        if x==20 or x==380 and y<225 or x==670 and y<225 or x== 745 and 250<y<540:
                        x_change=0
        if x==905 or x==545 and y<225 or x==255 and y<225 or x==180 and 250<y<540:
                        x_change=0
        if y==645 or y==250 and 180<x<745:
                        y_change =0
        if y==155 or y==225 and 255<x<380 or y==225 and 545<x<670 or y==540 and 180<x<745:
                        y_change = 0

        if x==20 and 400<y<520:
            LOK13_1()


        for Arrow in Arrows:
            if Arrow.d_stand==1 or Arrow.d_stand==-1:
                if Arrow.x<=display_width and x>=0:
                    Arrow.x+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
            else:
                if Arrow.x<=display_width and x>=0:
                    Arrow.y+=Arrow.speed
                else:
                    Arrows.pop(Arrows.index(Arrow))
                    
        for Arrow in Arrows:
            Arrow.draw()
            for Angry in Targets:
                if Arrow.x>=Angry.xm and Arrow.x<=Angry.xm+35 and Arrow.y>=Angry.ym and Arrow.y<=Angry.ym+50:
                    Angry.health-=15
                if Angry.health<=0:
                    Targets.pop(Targets.index(Angry))

        for Angry in Targets:
            if abs(x-Angry.xm)<=500 and abs(y-Angry.ym)<=400:
                if x==Angry.xm and y==Angry.ym:
                    Angry.TargetFront(dt)
                    Angry.m_direct=0
                    Health-=3
                if y>Angry.ym:
                    Angry.ym+=Angry.speed
                    Angry.m_direct=1
                elif y<Angry.ym:
                    Angry.ym-=Angry.speed
                    Angry.m_direct=-1
                if x<Angry.xm:
                    Angry.xm-=Angry.speed
                    Angry.m_direct=-2
                elif x>Angry.xm:
                    Angry.xm+=Angry.speed
                    Angry.m_direct=2
                Angry.Walking(dt)
            else:
                Angry.StandFront()
        

        WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)

        if Health<=0:
            DEADEND()
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)

def LOK13_1():
    x = 480
    y = 645
    xm=650
    ym=400
    x_change = 0
    y_change = 0
    d_stand = 2
    m_direct =0
    f_shooting = 0
    dt=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    print('(',x,',',y,')')
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    print('(',x,',',y,')')
                
                if event.key == pygame.K_SPACE:
                    f_shooting = 0
            
        screen.fill(black)
        x +=x_change
        y +=y_change
        screen.blit(Lok13_1,(0,0))

        if x!=480:
            x_change=5
        else:
            x_change=0
        if y!=450:
            y_change=-5
        else:
            y_change=0
        if x==480 and y == 450:
            CHAT4() 



        d_stand=-2

        WalkingOrShootingElsa(dt,x,y,x_change,y_change,d_stand,f_shooting)
        
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)


        
def Final():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        screen.fill(black)
        screen.blit(DEAD_END, (0,0))
        message_display('Из-за вашей наивности вас растерзали монстры',(display_width/2),500)
        button('Я смогу лучше', 150,500,250,50,green,bright_green,LOK1)
        button('Это невозможно ', 550,500,250,50,red,bright_red,quitgame)
        gameDisplay.blit(screen,(0,0))
        pygame.display.flip()
        dt=clock.tick(40)
        
LOK1()
             
pygame.quit()
quit()
