import numpy as np
from scipy.misc import imsave
from scipy.interpolate import interp1d

C_X = 0.255
C_Y = 0

CANVAS_HEIGHT = 1000
CANVAS_WIDTH = 1000

RANGE_MIN = -1.5
RANGE_MAX = 1.5

ITR_MAX = 200
INF = 4

def isInJuliaSet(x, y):
   for i in range(ITR_MAX):
      x2 = x * x - y * y + C_X
      y2 = 2 * x * y + C_Y
   
      x = x2
      y = y2

      if x*x + y*y > INF:
         return (False, i)
   return (True, 0) 

map_x = interp1d([0, CANVAS_WIDTH], [RANGE_MIN, RANGE_MAX])
map_y = interp1d([0, CANVAS_HEIGHT], [RANGE_MAX, RANGE_MIN])
map_c = interp1d([0, ITR_MAX], [0, 255])     # 255, 0 -> mostly white

canvas = np.full((CANVAS_HEIGHT, CANVAS_WIDTH), 255)  # 0 -> mostly white

for i in range(CANVAS_HEIGHT):
   for j in range(CANVAS_WIDTH):
      (flag, itr) = isInJuliaSet(map_x(j), map_y(i))
      if not flag:
         canvas[i][j] = int(map_c(itr))

# print(np.amax(canvas))
# print(canvas)
# print(canvas[633][700])
# print(canvas[634][700])
imsave("img" + str(ITR_MAX) + "_c_x" + str(C_X) + "_y" + str(C_Y) + ".png", canvas)

