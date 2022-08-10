import numpy as np

def startwith(start: int, w: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(w)) if x != start]
    dis = w[start]
    
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: 
                idx = i

        nopass.remove(idx)
        passed.append(idx)
    
        for i in nopass:
            if dis[idx] + w[idx][i] < dis[i]: 
                dis[i] = dis[idx] + w[idx][i]
    
    return dis,passed

if __name__ == "__main__":
    inf = np.inf
    w =[
        [0,1,12,inf,inf,inf],
        [inf,0,9,3,inf,inf],
        [inf,inf,0,inf,5,inf],
        [inf,inf,4,0,13,15],
        [inf,inf,inf,inf,0,4],
        [inf,inf,inf,inf,inf,0]
         ]

    dis,passed = startwith(0, w)
    print("距离最小为： ", dis[-1])
    print("最佳路径为： ",passed)