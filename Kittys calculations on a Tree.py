# working solution, however gets stuck on some cases due to time complexity
# feel free to change if you have an idea
from collections import defaultdict
from itertools import combinations

n, q = [int(i) for i in input().split()]

edges = defaultdict(set)


for line in range(n-1):
    a,b = [int(i) for i in input().split()]
    edges[a].add(b)
    edges[b].add(a)
    
def distance(beginning, end, dist):
    if not options[beginning]:
        return 0
    if end in options[beginning]:
        return dist + 1
    
    next_ = options[beginning]
    for n in next_:
        options[n].discard(beginning)
        
    return sum([distance(end, n, dist+1) for n in next_])
    
            
for set_def in range(q):

    k = input()
    query = {int(s) for s in input().split()}
    
    if len(query) == 1:
        print(0)
        continue
    
    comb = combinations(query,2)
    options = edges.copy()
    print(sum([a*b*(distance(a,b,0)) for a,b in comb])%(10**9 + 7))