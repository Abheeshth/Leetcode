class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        def addEdge(adj, u, v):
            adj[u].append(v)
            adj[v].append(u)
            
        for road in roads:
            addEdge(adj,road[0],road[1])
        dic = {}
        for i,val in enumerate(adj):
            dic[i] = len(val)
        
        sorted_dic = sorted(dic.items(),key = lambda x:x[1])
        dic2 = {}
        i = 1
        for j in sorted_dic:
            dic2[j[0]] = i
            i+=1
        sum1 = 0
        #print(dic2)
        for road in roads:
            sum1+=(dic2[road[0]])
            sum1+=(dic2[road[1]])
            print(sum1)
        #print(dic2)
        return sum1
        #print(adj)
            
        
        
        
        
        
        
        
        
        
        
