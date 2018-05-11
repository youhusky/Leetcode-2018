class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = collections.defaultdict(set)
        for p1, p2 in edges:
            children[p1].add(p2)
            children[p2].add(p1)
        #print children 
        edge = children.keys()
        while len(edge) > 2:
            leaves = [x for x in children if len(children[x]) == 1]
            for leaf in leaves:
                for parent in children[leaf]:
                    children[parent].remove(leaf)
                children[leaf] = ()
                edge.remove(leaf)
        return list(edge) if n > 1 else [0]
        
        
        
        
        
        
        
        
        

        
        