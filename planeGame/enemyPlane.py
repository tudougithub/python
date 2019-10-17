'''
@Descripttion: 敌机
@version: 1.0
@Author: 土豆
@Date: 2019-08-29 20:24:19
@LastEditors: 土豆
@LastEditTime: 2019-08-30 22:12:22
'''
import pygame
import gameSprite
import random
class Enemy(gameSprite.GameSprite):
    def __init__(self, enemyType = 1):
        #敌机类型
        self.type = enemyType
        self.image = "./image/Small.png"
        x = 512 - 60
        #血量
        self.blood = 5
        if enemyType == 2:
            self.image = "./image/Medium.png"
            x = 512 - 100
            self.blood = 10
        elif enemyType == 3:
            self.image = "./image/Big.png"
            x = 512 - 152
            self.blood = 30
        ##速度
        self.speed = random.randint(1, 3)
        super().__init__(self.image, self.speed)
        self.rect.x = random.randint(0, x)
        self.rect.y = -self.rect.bottom
    
    def update(self):
        super().update()
        if self.rect.y > 600:
            self.kill()








