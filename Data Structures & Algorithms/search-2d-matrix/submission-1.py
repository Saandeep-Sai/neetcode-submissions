class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in matrix:
            if i[0]<=target and i[len(i)-1] >= target:
                low = 0
                high = len(i) - 1
                while low <=high:
                    mid = (low+high)//2
                    if i[mid] == target:
                        return True
                    elif i[mid] < target:
                        low = mid + 1
                    elif i[mid] > target:
                        high = mid - 1
        return False