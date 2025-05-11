
G = []

def DFS(start):
    visit[start] = True

    for i in G[start]:
        if visit[i] == False:
            visit[i] = start

            DFS(i)

    return
