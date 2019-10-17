'''
@Descripttion: 游戏精灵
@version: 1.0
@Author: 土豆
@Date: 2019-08-29 09:47:44
@LastEditors: 土豆
@LastEditTime: 2019-08-29 18:31:53
'''

import pygame

class GameSprite(pygame.sprite.Sprite):
    '''
    初始化函数用于加载图片，默认设置图片移动速度为1
    '''
    def __init__(self, image, speed = 1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        super().update()
        self.rect.y += self.speed