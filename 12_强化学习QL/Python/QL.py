import numpy as np
import cv2 as cv
import copy
np.random.seed(0)
#array -> end is game end 
end = np.random.randint(0,10,2)

#dif is trap
dif = np.random.randint(0,10,(5,2))

#bz is epoch
bz = 100

# now is cube for position
now = [0,0]
tabl = np.zeros((10,10,4))
# img is canvas of game
img = np.zeros((500,500,3))
def choose(now,tabl):
    if np.random.rand() > 0.1 and np.sum(tabl[now[0], now[1], :]) != 0:
        ord = np.argmax(tabl[now[0], now[1], :])
    else:
        ord = np.random.randint(0,4,1)[0]
    go = now.copy()
    
    if ord == 0:
        #上下左右
        if go[0] != 0:
            go[0] = go[0] - 1
            
    elif ord == 1:  
        if go[0] != 9:
            go[0] = go[0] + 1
            
    elif ord == 2:  
        if go[1] != 0:
            go[1] = go[1] - 1
            
    elif ord == 3:  
        if go[1] != 9:
            go[1] = go[1] + 1
    return go,ord

def fs(now,go,tabl,end,ord,dif):
    if go[0] == end[0] and go[1] == end[1]:
        r = 1
    else:
        for i in range(5):
            if go[0] == dif[i,0] and go[1] == dif[i,1]:
                r = -1
                break
            else:
                r = 0
    tabl[now[0], now[1], ord] = tabl[now[0], now[1], ord] + 0.9*(r + 0.8*np.max(tabl[go[0], go[1], :]) - tabl[now[0], now[1], ord])
    
    return tabl

while bz:  
    img = np.zeros((500,500,3))
    go, ord = choose(now, tabl)
    
    tabl = fs(now, go, tabl, end, ord, dif)
    
    for i in range(5):
        cv.rectangle(img,(dif[i,1]*50,dif[i,0]*50),(dif[i,1]*50+50,dif[i,0]*50+50),(0,0,255),-1,4)
    cv.rectangle(img,(end[1]*50,end[0]*50),(end[1]*50+50,end[0]*50+50),(255,255,255),-1,4)
    for i in range(10):
        for j in range(10):
            cv.rectangle(img,(i*50,j*50),(i*50+50,j*50+50),(255,255,0),2,4)
    cv.rectangle(img,(now[1]*50,now[0]*50),(now[1]*50+50,now[0]*50+50),(255,0,0),-1,4)
    
    now = go
    
    if go[0] == end[0] and go[1] == end[1]:
        bz -= 1
        now = [0,0]
    cv.imshow("winname", img)
    cv.waitKey(10)
cv.waitKey(0)     
    