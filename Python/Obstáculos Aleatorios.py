from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
rojo = [248, 0, 0]
azul = [0, 20, 248]
obs1x1 = 0
obs2x2 = 0

sense.clear()

#Obstaculos 1x1
while obs1x1 != 10:
  x = random.randint(0,7)
  y = random.randint(0,7)
  sense.set_pixel(x, y, rojo)
  obs1x1 = obs1x1 + 1
  
#Obstaculos 2x2
while obs2x2 != 3:
  numobs2x2 = random.randint(0,10)
  numbobs2x2 = 1
  for x in range(0,2):
    for y in range(0,2):
      sense.set_pixel(x, y, rojo)
  
  numbobs2x2 = 2
  for x in range(6,8):
    for y in range(6,8):
      sense.set_pixel(x, y, rojo)
  
  numbobs2x2 = 3
  for x in range(2,4):
    for y in range(2,4):
      sense.set_pixel(x, y, rojo)
      
  numbobs2x2 = 5
  for x in range(6,7):
    for y in range(5,6):
      sense.set_pixel(x, y, rojo)
  
  numbobs2x2 = 6
  for x in range(3,4):
    for y in range(7,8):
      sense.set_pixel(x, y, rojo)
      
  numbobs2x2 = 7
  for x in range(4,5):
    for y in range(3,4):
      sense.set_pixel(x, y, rojo)
      
  numbobs2x2 = 8
  for x in range(7,8):
    for y in range(2,3):
      sense.set_pixel(x, y, rojo)
      
  numbobs2x2 = 9
  for x in range(6,7):
    for y in range(7,8):
      sense.set_pixel(x, y, rojo)
      
  numbobs2x2 = 10
  for x in range(5,6):
    for y in range(0,2):
      sense.set_pixel(x, y, rojo)

posFantasma = (0, 7, azul)
movAleatorio = random.randint(1,4)

  for movAleatorio():
    sense.set_pixel(posFantasma)
  
if movAleatorio == 1:
  sense.set_pixel(posFantasma)

if movAleatorio == 2:
  sense.set_pixel(posFantasma)
  
if movAleatorio == 3:
  sense.set_pixel(posFantasma)
  
if movAleatorio == 4:
  sense.set_pixel(posFantasma)