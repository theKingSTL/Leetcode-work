class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        for i, val in enumerate(arr):
            if i == 0:
                minDiff = arr[i+1] - arr[i]
                result = [[arr[i], arr[i+1]]]
            #we already eveluated that value and we dont want the values to == each other 
            elif arr[i] == arr[i-1]:
                continue 
            elif i < len(arr) - 1:
                midMin = arr[i+1] - arr[i]
                if midMin < minDiff:
                    minDiff = midMin
                    result = [[arr[i], arr[i+1]]]
                elif midMin > minDiff:
                    continue 
                else:
                    result.append([arr[i], arr[i+1]])
            else:
                print("ERROR: got to else branch")
        return result 
