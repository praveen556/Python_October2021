class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        A = list(accumulate(diff, initial = 0))
        return max(0, (upper - lower) - (max(A) - min(A)) + 1)




        
