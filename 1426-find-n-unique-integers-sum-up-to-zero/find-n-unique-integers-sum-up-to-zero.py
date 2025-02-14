class Solution:
    def sumZero(self, n: int) -> List[int]:

        # n = 5
        # [0, 1, 2, 3, -6]
        res = []
        if n == 1:
            return [0]

        res = [i for i in range(1, n)]
        res.append(-1*sum(res))

        return res        
        