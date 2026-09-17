# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/danie/Desktop/Daniel Lisboa/Curso em vídeo/Python/Python_3-Mundo_1/Exercícios/sound/021.wav')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
   pygame.time.Clock().tick(10)