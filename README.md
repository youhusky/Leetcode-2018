 Easy   96/213 ( 45.07 %)  ██████████████░░░░░░░░░░░░░░░░  
 Medi   84/382 ( 21.99 %)  ███████░░░░░░░░░░░░░░░░░░░░░░░  
 Hard   17/161 ( 10.56 %)  ████░░░░░░░░░░░░░░░░░░░░░░░░░░  

 public int numberOfGroup(Set<DLinkedNode> set){
        Map<DLinkedNode, Integer> map = new HashMap<>();
        . From 1point 3acres bbs
        int count = 0;. 
        for(DLinkedNode node : set){
            count++;.
            int sameGroup= map.getOrDefault(node, 0);
            count -= sameGroup;
            
            if(node.pre!=null). more info on 1point3acres.com
                map.put(node.pre, map.getOrDefault(node.pre, 0)+1);
            if(node.post!=null)
                map.put(node.post, map.getOrDefault(node.post, 0)+1);
        }
        
        return count;
    }