class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False

        for i in matrix:
            if i[0]<=target and i[len(i)-1] >= target and not found:
                for j in i:
                    if j == target:
                        found = True
                        break
            if found:
                break  
        return found 