import sense_hat
import random
import time

sense = sense_hat.SenseHat()

sense.clear()
s = sense

while True:
  for x in range(8):
    for y in range(0,2):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorR, colorG, colorB)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(6,8):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorR, colorG, colorB)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(8):
    for y in range(6,8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorR, colorG, colorB)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(0,2):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorR, colorG, colorB)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(2,6):
    for y in range(2,6):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorR, colorG, colorB)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(8):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorR, colorG, colorB)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(8):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.1)
  s.clear()
  
  for x in range(1):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(2):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(3):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(4):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(5):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(6):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(7):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(8):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(8):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(7):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(6):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(5):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(4):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(3):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(2):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()
  
  for x in range(1):
    for y in range(8):
      colorR = random.randint(0,255)
      colorG = random.randint(0,255)
      colorB = random.randint(0,255)
      sense.set_pixel(x, y, colorG, colorB, colorR)
      
  time.sleep(0.15)
  s.clear()