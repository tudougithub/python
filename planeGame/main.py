'''
@Descripttion: main
@version: 1.0
@Author: 土豆
@Date: 2019-08-29 09:10:40
@LastEditors: 土豆
@LastEditTime: 2019-08-31 21:04:43
'''

import pygame
import random
import background
import hero
import enemyPlane
import bullet
START_GAME = 1  #开始游戏
END_GAME = 2    #退出

EVENT_CREATE_ENEMY = pygame.USEREVENT #创造敌机事件
EVENT_CREATE_BULLET = pygame.USEREVENT + 1 #创造子弹事件

screen = pygame.display.set_mode((512, 600))

class GameMain():
    
    def __init__(self):
        #两个游戏背景图片
        self.bg1 = background.Background("./image/Background.jpg")
        self.bg2 = background.Background("./image/Background.jpg")
        self.bg2.rect.y = -self.bg2.rect.bottom
        self.bgGroup = pygame.sprite.Group(self.bg1, self.bg2)

        self.clock = pygame.time.Clock()

        ##英雄
        self.hero = hero.Heao()
        self.heroGroup = pygame.sprite.Group(self.hero)

        #敌机
        self.enemyGroup = pygame.sprite.Group()
        pygame.time.set_timer(EVENT_CREATE_ENEMY, 500)

        #子弹
        self.bulletGroup = pygame.sprite.Group()
        pygame.time.set_timer(EVENT_CREATE_BULLET, 500)

        #分数
        self.score = 0

    ##开始游戏
    def startGame(self):
        while True:
            self.clock.tick(1000)
            self.__drawAll()
            self.__event()
            if self.__collider():
                break
            

    ##创造敌机
    def __createEnemy(self):
        enemyType = random.randint(1, 3)
        enemy = enemyPlane.Enemy(enemyType)
        self.enemyGroup.add(enemy)
    
    ##创造子弹
    def __createBullet(self, isSuper = False):
        img = "./image/Bullet.png"
        if isSuper:
            img = "./image/SuperBullet.png"
            for i in [1, 2]:
                b = bullet.Bullet(img, 1)
                b.rect.x = self.hero.rect.centerx
                b.rect.y = self.hero.rect.y - 30 * i
                self.bulletGroup.add(b)
        else:
            for i in [1, 2, 3, 4, 5]:
                b = bullet.Bullet(img, 3)
                b.rect.x = self.hero.rect.centerx
                b.rect.y = self.hero.rect.y - 30 * i
                self.bulletGroup.add(b)


    ##碰撞检测
    def __collider(self):
        #子弹与敌机的碰撞检测
        #返回字典，子弹为键，敌机为值
        tt = pygame.sprite.groupcollide(self.bulletGroup, self.enemyGroup, True, False)
        if len(tt) > 0:
            for (key, value) in tt.items():
                value[0].blood -= key.atk
                if value[0].blood <= 0:
                    x = value[0].rect.x
                    y = value[0].rect.y
                    type = value[0].type
                    self.enemyGroup.remove(value[0])
                    self.__drawBoom(type, x, y)
                    self.score += value[0].type
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("./audio/meteorit_explode.wav")
                    sound.play()
                    
        #敌机与英雄的碰撞检测        
        flag = pygame.sprite.spritecollide(self.hero, self.enemyGroup, True)
        if len(flag) > 0:
            self.__gameOver()
            return 1
    ##绘制爆炸效果
    def __drawBoom(self, type, x, y):
            for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                image = "./image/blow" + str(type) +"_" + str(i) + ".png"
                blow = pygame.image.load(image)
                screen.blit(blow, (x, y))
                pygame.display.update()
    ##游戏结束
    def __gameOver(self):
        startButton = pygame.image.load("./image/startButton.png")
        exitButton = pygame.image.load("./image/exitButton.png")
        screen.blit(startButton, (130, 300))
        screen.blit(exitButton, (130, 350))
        pygame.display.update()
    
    ##绘制图像
    def __drawAll(self):
        #背景
        self.bgGroup.update()
        self.bgGroup.draw(screen)

        #我方英雄
        self.heroGroup.update()
        self.heroGroup.draw(screen)
        
        #敌机
        self.enemyGroup.update()
        self.enemyGroup.draw(screen)

        #子弹
        self.bulletGroup.update()
        self.bulletGroup.draw(screen)

        #分数
        text = "score:" + str(self.score)
        myFont = pygame.font.SysFont("arial", 30)
        t = myFont.render(text, True, (0, 0, 0))
        screen.blit(t,(10, 10))

        pygame.display.update()

        

    #事件监听
    def __event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == EVENT_CREATE_ENEMY:
                self.__createEnemy()
            elif event.type == pygame.KEYDOWN:
                #按空格触发超级子弹
                if event.key == pygame.K_SPACE:
                    self.__createBullet(True)
            elif event.type == EVENT_CREATE_BULLET:
                self.__createBullet()
            



#游戏初始化
def gameInit():
    pygame.init()
    pygame.display.set_caption("飞机大战")

    pygame.mixer.init()
    pygame.mixer.music.load("./audio/bgm_zhuxuanlv.mp3")
    # -1表示背景音乐循环播放
    pygame.mixer.music.play(-1)    
    #初始化背景图片
    startBackground = pygame.image.load("./image/BgLogo.jpg")
    logo = pygame.image.load("./image/LOGO.png")
    startButton = pygame.image.load("./image/startButton.png")
    exitButton = pygame.image.load("./image/exitButton.png")
    screen.blit(startBackground, (0, 0))
    screen.blit(logo, (-30, 40))
    screen.blit(startButton, (130, 300))
    screen.blit(exitButton, (130, 350))
    pygame.display.update()

##初始化中的事件监听
def initEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if (x >= 130 and x <= 130+266) and (y >= 300 and y <= 300+39):
                return START_GAME
            elif (x >= 130 and x <= 130+266) and (y >= 350 and y <= 350+39):
                return END_GAME
    

if __name__ == '__main__':
    gameInit()
    while True:
        event = initEvent()
        ##点击startGame开始游戏
        if event == START_GAME:
            break
        ##点击exit退出游戏
        elif event == END_GAME:
            pygame.quit()
            exit(0)
    gm = GameMain()
    gm.startGame()
    
    while True:
        pygame.mouse.set_visible(True)
        event = initEvent()
        ##点击startGame开始游戏
        if event == START_GAME:
            game = GameMain()
            game.startGame()
        ##点击exit退出游戏
        elif event == END_GAME:
            pygame.quit()
            exit(0)
    



