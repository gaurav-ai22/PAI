from sys import maxsize 
from itertools import permutations

V=4

def travellingSalesmanProblem(graph, s): 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 

    min_path = maxsize 
    next_permutation = permutations(vertex)
    final_path = None
    for i in next_permutation:
        current_pathweight = 0
        k = s 
        path = [s]
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
            path.append(k)
        current_pathweight += graph[k][s] 
        path.append(s)

        if current_pathweight < min_path:
            min_path = current_pathweight
            final_path = path
            
    return min_path, final_path

if __name__ == "__main__": 
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]] 
    s = 0
    min_path_cost, min_path = travellingSalesmanProblem(graph, s)
    print("Minimum Path Cost:", min_path_cost)
    print("Path Taken:", min_path)
