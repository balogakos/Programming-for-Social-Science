import random

# Make a y0,x0 variables.

y0 = 50
x0 = 50
# Change y0 and x0 based on random numbers 3 times.


if random.random() < 0.5:
    y0+= 1
else:
    y0-= 1
if random.random() < 0.5:
    x0+= 1
else:
    x0-= 1
    
if random.random() < 0.5:
    y0+= 1
else:
    y0-= 1
if random.random() < 0.5:
    x0+= 1
else:
    x0-= 1
    
if random.random() < 0.5:
    y0+= 1
else:
    y0-= 1
if random.random() < 0.5:
    x0+= 1
else:
    x0-= 1

# Make a y1,x1 variables.

y1 = 50
x1 = 50

# Change y1 and x1 based on random numbers 3 times


if random.random() < 0.5:
    y1+= 1
else:
    y1-= 1
if random.random() < 0.5:
    x1+= 1
else:
    x1-= 1

if random.random() < 0.5:
    y1+= 1
else:
    y1-= 1
if random.random() < 0.5:
    x1+= 1
else:
    x1-= 1

if random.random() < 0.5:
    y1+= 1
else:
    y1-= 1
if random.random() < 0.5:
    x1+= 1
else:
    x1-= 1

#find the distance using pythag thereom

diffx = x1 - x0
diffy = y1 - y0

ansx = (diffx*diffx)
ansy = (diffy*diffy)

answer = (ansx + ansy)**0.5

print (answer)


