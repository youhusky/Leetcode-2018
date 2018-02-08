class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(candidates, target, res, [], 0)
        return res
    def backtracking(self, candidates, target, res ,temp, start):
        if target < 0:
            return
        elif target == 0:
            res.append(list(temp))
        else:
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                # can use mutilple
                self.backtracking(candidates, target - candidates[i], res, temp, i)
                temp.pop()
                
