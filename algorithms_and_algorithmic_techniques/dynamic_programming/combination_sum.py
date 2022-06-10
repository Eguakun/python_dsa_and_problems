# Naive solution: Make a decision tree and try every possible combination
# This works but it will produce duplicate values 

'''

Naive  [2,3,6,7] target = 7

             2                                           
           /   \
         /      \
       2,2      2,3     2,6 or 2, 7
      /           \
    /              \                   
    2,2,3            2,3,2 duplicates  
                  
                  
             3 
           /   \
         /      \
      /           \
    /              \       
    
    
             6 all of these above the target
           /   \
         /      \
       6,2      6,3   6,6 or 6,7
      /           \
    /              \
    
    
    
             7 Already at target 
           /   \
         /      \    
      /           \
    /              \                   


'''

'''
Optimized solution 
Make sure that no 2s show up in the right side and that way we can prevent duplicates

                         . 
                       /   \
                     /      \    
                  /           \
                /              \   
               2                \
              / \(no more 2s)    \
             /    [2]             3,6,7
        [2,2]       \  
          /        [2,2]
         /          /   \ 
    [2,2,2]     [2,2,3]  [2,2] (this path would try  and 7 which would go above the target)
    
    
    recursive 
    
    
    
'''


# Time complexity: making two decision trees so height of decision tree
# 2 ^ T where t is the target value

def combinationSum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return


        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        cur.pop()

        dfs(i + 1, cur, total)
    dfs(0, [], 0)
    return res
