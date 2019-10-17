'''
@Descripttion: 设置背景
@version: 1.0
@Author: 土豆
@Date: 2019-08-29 09:26:20
@LastEditors: 土豆
@LastEditTime: 2019-08-31 21:02:44
'''

import pygame
import gameSprite


class Background(gameSprite.GameSprite):
    def __init__(self, image):
        super().__init__(image)
    def update(self):
        super().update()
        #如果y坐标大于768就置为-768，使背景图片循环播放
        if self.rect.y > 768:
            self.rect.y = -768


