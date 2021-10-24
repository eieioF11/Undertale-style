#!/usr/bin/env python
# -*- coding: utf-8 -*-
### インポート
import sys
import time
from typing import Collection
import pygame
from pygame.locals import *
from Timer import Timer
from GameIO import *

from Attack import *

import random

### 設定
D_SIZE_X     = 700      #windowサイズ
D_SIZE_Y     = 500
B_SIZE       = 200
B_POS_X      = D_SIZE_X//2
B_POS_Y      = D_SIZE_Y//2+60
P_SPD        = 5
MAX_HP       = 20
HP_POS_X     = B_POS_X-B_SIZE//2-60
HP_POS_Y     = B_POS_Y+B_SIZE//2+10
BONE_MAX_H   = 180
BONE_MIN_H   = 10
BAL_SIZE     = 10       # ボールサイズ
F_RATE       = 60       # フレームレート
K_REPEAT     = 20       # キーリピート発生間隔
BAL_SPD      = 10       # ボール移動速度
F_SIZE       = 60       # フォントサイズ
S_TIME       = 1        # START画面時間(秒)
E_TIME       = 2        # CLEAR画面時間(秒)

### 画面定義(X軸,Y軸,横,縦)
SURFACE  = Rect(0, 0, D_SIZE_X, D_SIZE_Y) # 画面サイズ

class player:
    def __init__(self,surface,img):
        self.surface=surface
        self.img=img
        self.x=B_POS_X
        self.y=B_POS_Y
        self.hp=MAX_HP
        self.hpflag=False
        self.hitflag=False
        self.Hit=0
        self.t1=Timer()
        self.t2=Timer()
        self.t3=Timer()
    def addx(self,add):
        self.x+=add
    def addy(self,add):
        self.y+=add
    def HP(self):
        return self.hp
    def pos(self):
        return [self.x,self.y]
    def update(self,Hit):
        if self.x<(B_POS_X-(B_SIZE//2))+(self.img.get_width()//2):
            self.x=(B_POS_X-(B_SIZE//2))+(self.img.get_width()//2)
        if self.x>(B_POS_X+(B_SIZE//2))-(self.img.get_width()//2):
            self.x=(B_POS_X+(B_SIZE//2))-(self.img.get_width()//2)
        if self.y<(B_POS_Y-(B_SIZE//2))+(self.img.get_height()//2):
            self.y=(B_POS_Y-(B_SIZE//2))+(self.img.get_height()//2)
        if self.y>(B_POS_Y+(B_SIZE//2))-(self.img.get_height()//2):
            self.y=(B_POS_Y+(B_SIZE//2))-(self.img.get_height()//2)
        if Hit:
            self.Hit=Hit
        if self.Hit:
            if not self.hpflag:
                self.hp-=Hit
                self.hpflag=True
            if self.t2.stand_by(100) and not self.hitflag:
                self.t3.reset()
                self.hitflag=True
            if self.hitflag:
                if self.t3.stand_by(100):
                    self.t2.reset()
                    self.hitflag=False
            else:
                self.surface.blit(self.img, (self.x-(self.img.get_width()//2),self.y-(self.img.get_height()//2)))
            if self.t1.stand_by(1000):
                self.t2.reset()
                self.t1.reset()
                self.Hit=0
                self.hpflag=False
                self.hitflag=False
        else:
            self.surface.blit(self.img, (self.x-(self.img.get_width()//2),self.y-(self.img.get_height()//2)))

class bone(Attack_object):
    def __init__(self,surface,x,y,h,Lim=[BONE_MIN_H,BONE_MAX_H],up=False):
        super().__init__(surface,x,y)
        self.up=up
        self.w=8
        self.h=h
        self.lim=0
        self.Lim=Lim
    def height(self,h):#height
        self.h=h
    def limit(self):
        return self.lim
    def update(self):
        if self.h>self.Lim[1]:
            self.lim=2
            self.h=self.Lim[1]
        elif self.h<self.Lim[0]:
            self.lim=1
            self.h=self.Lim[0]
        else:
            self.lim=0

        if self.up:
            pygame.draw.circle(self.surface, (255,255,255), (self.x,self.y+2+6), 5)
            pygame.draw.circle(self.surface, (255,255,255), (self.x+(self.w//2)+3,self.y+2+6), 5)
            pygame.draw.circle(self.surface, (255,255,255), (self.x,self.y+self.h+6), 5)
            pygame.draw.circle(self.surface, (255,255,255), (self.x+(self.w//2)+3,self.y+self.h+6), 5)
            pygame.draw.rect(self.surface,(255,255,255),Rect(self.x,self.y+6,self.w,self.h))
            if self.x<=self.player[0] and self.player[0]<=self.x+self.w and self.y<=self.player[1] and self.player[1]<=self.y+self.h+6:
                self.Collision=True
            else:
                self.Collision=False
        else:
            pygame.draw.circle(self.surface, (255,255,255), (self.x,self.y+2-self.h-8), 5)
            pygame.draw.circle(self.surface, (255,255,255), (self.x+(self.w//2)+3,self.y+2-self.h-8), 5)
            pygame.draw.circle(self.surface, (255,255,255), (self.x,self.y-8), 5)
            pygame.draw.circle(self.surface, (255,255,255), (self.x+(self.w//2)+3,self.y-8), 5)
            pygame.draw.rect(self.surface,(255,255,255),Rect(self.x,self.y-self.h-8,self.w,self.h))
            if self.x<=self.player[0] and self.player[0]<=self.x+self.w and self.y-self.h<=self.player[1] and self.player[1]<=self.y-8:
                self.Collision=True
            else:
                self.Collision=False

class bone_attack1(Attack):
    bones = []
    add=True
    dir=1#direction
    h=[70,70]
    flag1=False
    def update(self):
        if self.add:
            self.bones.append(bone(self.surface,B_POS_X-(B_SIZE//2)+10,B_POS_Y+(B_SIZE//2),70,[BONE_MIN_H,BONE_MAX_H-30]))
            self.bones.append(bone(self.surface,B_POS_X-(B_SIZE//2)+10,B_POS_Y-(B_SIZE//2),70,[BONE_MIN_H,BONE_MAX_H-30],True))
            self.dir=1
            self.add=False
        self.bones[0].player_pos(self.player)
        self.bones[1].player_pos(self.player)
        if self.bones[0].collision() or self.bones[1].collision():
            self.Collision=True
        else:
            self.Collision=False
        if self.flag1:
            self.h[0]+=1
            self.h[1]-=1
        else:
            self.h[0]-=1
            self.h[1]+=1
        for b in self.bones:
            if b==self.bones[0]:
                if b.limit()==1:
                    self.flag1=True
                b.height(self.h[0])
            else:
                if b.limit()==1:
                    self.flag1=False
                b.height(self.h[1])
            b.add(self.dir,0)
            b.update()
        if self.bones[0].return_x()>B_POS_X+(B_SIZE//2)-15 or self.bones[0].return_x()<B_POS_X-(B_SIZE//2)+10:
            self.dir*=-1
            return True
        return False

class HPshow:
    def __init__(self,surface):
        self.surface=surface
        self.images=[]
        for i in range(21):
            self.images.append(load_image("HP"+str(i).zfill(2)+".gif"))
    def update(self,hp):
        self.surface.blit(self.images[hp], (HP_POS_X,HP_POS_Y))

############################
### メイン関数
############################
def main():
    #音声読み込み

    ### 画像読み込み
    rhimg = load_image("redheart.png")
    rhimg = pygame.transform.scale(rhimg, (14,14))
    ### 画面初期化
    pygame.init()
    pygame.mixer.init()
    surface = pygame.display.set_mode(SURFACE.size)
    ### 時間オブジェクト生成
    clock = pygame.time.Clock()
    ### Object
    hpshow=HPshow(surface)
    p=player(surface,rhimg)
    attacks=[]
    t1=Timer()
    ### キーリピート有効
    pygame.key.set_repeat(K_REPEAT)
    ### 無限ループ
    attacks.append(bone_attack1(surface,B_POS_X-(B_SIZE//2),B_POS_Y+(B_SIZE//2)))
    while True:
        ### フレームレート設定
        clock.tick(F_RATE)
        ### 背景色設定
        surface.fill((0,0,0))
        ###描画処理
        pygame.draw.rect(surface,(255,255,255),Rect(B_POS_X-(B_SIZE//2),B_POS_Y-(B_SIZE//2),B_SIZE,B_SIZE),10,5)
        count=0
        for a in attacks:
            a.player_pos(p.pos())
            a.update()
            if a.collision():
                count+=1
        p.update(count)
        #print(p.HP())
        hpshow.update(p.HP())
        ### 画面更新
        pygame.display.update()
        ### 再生

        ### イベント処理
        for event in pygame.event.get():
            ### 終了処理
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                ### キー操作
                pygame.key.set_repeat(10, 20)
                if event.key == K_LEFT:
                    p.addx(-P_SPD)
                if event.key == K_RIGHT:
                    p.addx(P_SPD)
                if event.key == K_UP:
                    p.addy(-P_SPD)
                if event.key == K_DOWN:
                    p.addy(P_SPD)
                if event.key == K_SPACE:
                    pass

############################
### 終了関数
############################
def exit():
    pygame.quit()
    sys.exit()

############################
### メイン関数呼び出し
############################
if __name__ == "__main__":
    ### 処理開始
    main()