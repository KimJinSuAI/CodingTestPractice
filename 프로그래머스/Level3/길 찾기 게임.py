import sys
sys.setrecursionlimit(100000)
def preorder(tree, node, l):
    l+=[node[2]]
    if tree[node]["left"]!=():
        preorder(tree,tree[node]["left"],l)
    if tree[node]["right"]!=():
        preorder(tree,tree[node]["right"],l)
    return l
def postorder(tree, node, l):
    if tree[node]["left"]!=():
        postorder(tree,tree[node]["left"],l)
    if tree[node]["right"]!=():
        postorder(tree,tree[node]["right"],l)
    l+=[node[2]]
    return l

def solution(nodeinfo):
    tree = {}
    for index in range(len(nodeinfo)):
        nodeinfo[index].append(index+1)
    nodeinfo = list(map(tuple, sorted(nodeinfo, key = lambda x:(x[1],x[0]))))

    root = nodeinfo.pop()
    tree[root] = {"parent":(), "left":(), "right":()}
    for node in reversed(nodeinfo):
        parent = root
        while parent !=():
            before = parent
            if parent[0] > node[0]:
                parent = tree[parent]["left"]
                if parent == () :
                    tree[before]["left"] = node
            else:
                parent = tree[parent]["right"]
                if parent == ():
                    tree[before]["right"] = node

        tree[node] = {"parent":before, "left":(), "right":()}
        
    return [preorder(tree,root,[]), postorder(tree,root,[])]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))