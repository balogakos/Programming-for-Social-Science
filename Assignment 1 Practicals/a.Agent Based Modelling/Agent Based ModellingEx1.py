#import random library
import random
import doctest

# Make a y0,x0 variables, randomly assign starting coordinates using randint
y0 = random.randint(0,99)
x0 = random.randint(0,99)

#print(y0, x0)

# Change y0 and x0 based on random numbers 3 times.
if random.random() < 0.5:
    y0+= 1
else:
    y0-= 1
if random.random() < 0.5:
    x0+= 1
else:
    x0-= 1
    
#print(y0,x0) to check if random is working
    
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

#print(y0, x0), to check if changing values worked

# Make a y1,x1 variables, assign random starting coordinates
y1 = random.randint(0,99)
x1 = random.randint(0,99)
#print(y1, x1)

# Change y1 and x1 based on random numbers 3 times
if random.random() < 0.5:
    y1+= 1
else:
    y1-= 1
if random.random() < 0.5:
    x1+= 1
else:
    x1-= 1
#print(y1, x1)
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
#print(y1, x1)

#find the distance using pythag thereom
diffx = x1 - x0
diffy = y1 - y0

ansx = (diffx*diffx)
ansy = (diffy*diffy)

#implementing first simple function to practise doctesting
def pythag(x, y):
    '''
    

    Parameters
    ----------
    x : differnces in x, squared.
    y : differences in y, squared.

    Returns: the distance between two coordinates
    -------
    pythag(3, 4)
    '''
    answer = (x + y)**0.5
    print(answer)
    return answer
    
pythag(ansx, ansy)



