# stuck on 2 test cases due to time complexity, otherwise it runs
def swapNodes(indexes, queries):
    # Write your code here
    result = []
    
    def in_order(index, depth, query):
        if index == -1:
            return []
               
        if not depth%query:
            indexes[index-1] = indexes[index-1][::-1]
            
        return (in_order(indexes[index-1][0],depth+1,query)
                    + [index] + 
                    in_order(indexes[index-1][1],depth+1,query))
    
    for q in queries:

        result.append(in_order(1,1,q))

    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()