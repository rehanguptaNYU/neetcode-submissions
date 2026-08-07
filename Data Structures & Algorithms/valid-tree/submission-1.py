class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList={}
        if len(edges)!=(n-1):
            return False
        if len(edges)==0:
            return True
        for arr in edges:
            if arr[0] not in adjList:
                adjList[arr[0]]=[]
            if arr[1] not in adjList:
                adjList[arr[1]]=[]
            adjList[arr[0]].append(arr[1])
            adjList[arr[1]].append(arr[0])
        visited=set()
        length=0
        def dfs(node):
            if node in visited:
                return None
            visited.add(node)
            for neighbour in adjList[node]:
                dfs(neighbour)
        keys_list=list(adjList.keys())
        dfs(keys_list[0])
        if len(visited)==n:
            return True
        else:
            return False
            
            
