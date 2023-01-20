def DFS(step):
    if dm[step] > 0:
        return dm[step]
    if step==1 or step==2:
        return step
    else: 
        dm[step] = DFS(step-1) + DFS(step-2)
        return dm[step]


if __name__=="__main__":
    n = int(input())
    dm = [0]*(n+2)
    print(DFS(n+1))