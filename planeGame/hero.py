'''
@Descripttion: 游戏主角
@version: 1.0
@Author: 土豆
@Date: 2019-08-29 19:15:16
@LastEditors: 土豆
@LastEditTime: 2019-08-31 21:03:46
'''
import pygame
import gameSprite

class Heao(gameSprite.GameSprite):
    def __init__(self):
        super().__init__("./image/Hero.png")
        #设置鼠标位置，并获取
        pygame.mouse.set_pos(300, 450)
        pygame.mouse.set_visible(False)
        x, y = pygame.mouse.get_pos()
        self.x = x
        self.y = y
    def update(self):
        #我方飞机始终处于鼠标的中心位置
        x, y = pygame.mouse.get_pos()
        if x < self.rect.width / 2:
            x = self.rect.width / 2
        elif x > 512 - self.rect.width / 2:
            x = 512 - self.rect.width / 2
        if y < self.rect.height / 2:
            y = self.rect.height / 2
        elif y > 600 - self.rect.height / 2:
            y = 600 -self.rect.height / 2
        self.rect.centerx = x
        self.rect.centery = y


        