'''========================
       clock emulator
   ========================
   '''
from PIL import Image, ImageDraw
import time, math
local = time.localtime()
#print(local)
hour = local.tm_hour
minutes = local.tm_min


SIZE = (500, 500)
CENTER = (250, 250)
clock = Image.new('RGB', SIZE, 'white')
DRAW = ImageDraw.Draw(clock)

def coord(angle, center, radius):
 """Return (x,y) coordinates of a point in a circle."""
 rad = math.radians(540 - angle) #I didn't understand here
 x = int(center[0] + math.sin(rad) * radius)
 y = int(center[1] + math.cos(rad) * radius)
 return x, y


BOX = (50, 50, 450, 450)
h_x, h_y =coord((hour/12)*360, CENTER, 185)
m_x, m_y =coord((minutes/60)*360, CENTER, 185)
p1 = (h_x, h_y)
p2 =(m_x, m_y)
#print(p1, p2)
BOX = (50, 50, 450, 450)
DRAW.arc(BOX, 0, 360, fill='red')
DRAW.line((p1, CENTER), fill = 'green', width = 20)
DRAW.line((p2, CENTER), fill = 'blue', width = 10)
clock.save('clock.png')