import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# x1, y1, x2, y2 = map(int, input().split())
# x11, y11, x22, y22 = map(int, input().split())
x1, y1, x2, y2 = 4, 2, 9, 7
x11, y11, x22, y22  = 1, 8, 4, 9

width1, width2 =  x2-x1, x22-x11
height1, height2 =  y2-y1, y22-y11
rightFig = max(x2, x22)
leftFig = min(x1, x11)
print(rightFig, leftFig)
minWidth = rightFig - leftFig
highFig = max(y2, y22)
lowFig = min(y1, y11)
print(highFig, lowFig)
minHeight = highFig - lowFig
print(minWidth,minHeight)
actualLen = max(minWidth,minHeight)
print(actualLen**2)


fig, ax = plt.subplots()
ax.add_patch(Rectangle((x1, y1), width1, height1))
ax.add_patch(Rectangle((x11, y11),width2, height2, color='y'))
ax.add_patch(Rectangle((leftFig, lowFig),actualLen, actualLen, color='y', fill=False))

plt.xticks([1, 2, 3, 4, 5,6,7,8,9,10])
plt.yticks([1, 2, 3, 4, 5,6,7,8,9,10])

plt.show()
