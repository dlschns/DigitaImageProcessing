#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:31:37 2019

@author: Amelia Kosasih, Anang Bagus, Anugrah Prasetia , Delischa Novilda, Griselda Anjeli
"""

import numpy as np
import matplotlib.pyplot as plt

def gray(im,r,g,b):
    imgray = r*im[:,:,0]+g*im[:,:,1]+b*im[:,:,2]
    return (imgray)

def negatif(im):
    img = im.copy()
    img = 1 - img
    return(img)

def logtrans(im):
    img = im.copy()
    c = 1.0
    r = img
    s = c*np.log(1+r)
    return(s)

def powertrans(img,x,y):
    im = img.copy()
    c = x
    gamma = y
    result = c*im**gamma
    result[result>1.0] = 1.0
    return(result)
    
def color(img,r,g,b):
    result=img.copy()
    result[:,:,0] *= r
    result[:,:,1] *= g
    result[:,:,2] *= b
    result[result>1.0] = 1.0
    return (result)

def contrast(img,b,c):
    brightness = b
    contrast = c
    img = np.int16(img)
    img = img * (contrast/127+1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)
    return (img)

def image_enhancement(img,c,y,r,g,b):
    p1=img.copy()
    p2=powertrans(p1,c,y)
    result=color(p2,r,g,b)   
    return result

def scan_image(address):
    return (plt.imread(address)/255)

def RUN():
    citra = ['03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg','11.jpg','12.jpg']
    hasil3 = image_enhancement(scan_image(citra[0]),1,1.9,1.3,1.3,1.8)
    hasil4 = image_enhancement(scan_image(citra[1]),1,3.35,3.3,0.9,2.85)
    hasil5 = image_enhancement(scan_image(citra[2]),1,1.5,2,0.8,1.2)
    hasil6 = image_enhancement(scan_image(citra[3]),1,1.65,1.0,0.9,1.1)
    hasil7 = image_enhancement(scan_image(citra[4]),1,2.2,3,1.15,1.5)
    hasil8 = image_enhancement(scan_image(citra[5]),1,2,3,1.1,0.95)
    hasil9 = image_enhancement(scan_image(citra[6]),1,2.5,1,1.2,1.5)
    hasil10 = image_enhancement(scan_image(citra[7]),1,1.15,1.26,1.2,1.2)
    hasil11 = image_enhancement(scan_image(citra[8]),1,2,4,1.05,1.1)
    hasil12 = image_enhancement(scan_image(citra[9]),1,2.5,9,1.25,1.45)
    plt.subplot(251)
    plt.imshow(hasil3)
    plt.imsave('hasil_03.jpg',hasil3)
    plt.subplot(252)
    plt.imshow(hasil4)
    plt.imsave('hasil_04.jpg',hasil4)
    plt.subplot(253)
    plt.imshow(hasil5)
    plt.imsave('hasil_05.jpg',hasil5)
    plt.subplot(254)
    plt.imshow(hasil6)
    plt.imsave('hasil_06.jpg',hasil6)
    plt.subplot(255)
    plt.imshow(hasil7)
    plt.imsave('hasil_07.jpg',hasil7)
    plt.subplot(256)
    plt.imshow(hasil8)
    plt.imsave('hasil_08.jpg',hasil8)
    plt.subplot(257)
    plt.imshow(hasil9)
    plt.imsave('hasil_09.jpg',hasil9)
    plt.subplot(258)
    plt.imshow(hasil10)
    plt.imsave('hasil_10.jpg',hasil10)
    plt.subplot(259)
    plt.imshow(hasil11)
    plt.imsave('hasil_11.jpg',hasil11)
    plt.subplot(2,5,10)
    plt.imshow(hasil12)
    plt.imsave('hasil_12.jpg',hasil12)    
    plt.show()

if __name__ == '__main__':
    RUN()
    