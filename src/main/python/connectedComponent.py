edges = [[0,1], [1,2], [3,4], [1,3]]
n = 5

par = [i for i in range(n)]
rank = [1] * n
components = n

print(par)
print(rank)


def superNode(k):
    while not k == par[k]:
        k = par[k]
    return k

def resolve(edge):
    node1 = superNode(edge[0])
    node2 = superNode(edge[1])

    if node1 == node2:
        return 0

    rank1 = rank[node1]
    rank2 = rank[node2]

    if rank1 > rank2:
        rank[node1] += rank[node2]
        par[node2] = par[node1]
        return - 1
    else:
        rank[node2] += rank[node1]
        par[node1] = par[node2]
        return -1

for i in edges:
    components += resolve(i)

print(components)
print(par)
print(rank)