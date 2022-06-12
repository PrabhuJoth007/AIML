def alphabetapruning(alpha, beta, p, tree, node):
    if isinstance(node,int):
        print('Visited node ',node)
        return node
    ans = ''
    player = ''
    if p==-1:
        for c in range(len(tree[node])):
            child = tree[node][c]
            beta = min(beta,alphabetapruning(alpha,beta,p*-1,tree,child))
            if beta<=alpha and tree[node][c+1:]!=[]:
                print('Pruning : ',tree[node][c+1:])
                break
        ans = beta
        player = 'Min'
    elif p==1:
        for c in range(len(tree[node])):
            child = tree[node][c]
            alpha = max(alpha,alphabetapruning(alpha,beta,p*-1,tree,child))
            if alpha >=beta and tree[node][c+1:]!=[]:
                print('Pruning : ',tree[node][c+1:])
                break
        ans = alpha
        player = 'Max'
    print('Visited node '+node+' as '+player+' and returning ',ans," ", (alpha, beta))
    return ans

tree = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [3,5],
    'E' : [6,9],
    'F' : [1,2],
    'G' : [0,-1]
}
alphabetapruning(-float('inf'), float('inf'), 1, tree, 'A')
