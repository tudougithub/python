'''
@Descripttion: 子弹
@version: 1.0
@Author: 土豆
@Date: 2019-08-30 20:12:58
@LastEditors: 土豆
@LastEditTime: 2019-08-30 21:55:25
'''

import gameSprite
import pygame
class Bullet(gameSprite.GameSprite):
    def __init__(self, image, atk):
        #攻击力
        self.atk = atk
        super().__init__(image)
    def update(self):
        super().update()
        self.rect.y -= 4
        if self.rect.y < 0:
            self.kill()