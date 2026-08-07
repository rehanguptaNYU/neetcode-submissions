class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={}
        visited=set()
        if len(prerequisites)==0:
            return True
        for i in range(len(prerequisites)):
            arr1=prerequisites[i]
            if arr1[0] not in preMap:
                preMap[arr1[0]]=[]
            if arr1[1] not in preMap:
                preMap[arr1[1]]=[]
            preMap[arr1[0]].append(arr1[1])
        keys_list=list(preMap.keys())
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if len(preMap[node])==0:
                visited.remove(node)
                return True
            for i in preMap[node]:
                bool_val=dfs(i)
                if bool_val==False:
                    return False
            visited.remove(node)
            preMap[node]=[]
            return True
        key_list=list(preMap.keys())
        for i in key_list:
            val=dfs(i)
            if val==False:
                return False
        return True
    
        

        
        
        
            