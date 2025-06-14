class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        count = 0
        l = 0
        for i in range(k):
            total += arr[i]
        average = total / k
        if average >= threshold:
            count += 1
        for r in range(k, len(arr)):
            total -= arr[l]
            l += 1
            total += arr[r]
            average = total / k
            if average >= threshold:
                count += 1
        return count


"""
    avg of subarray >= threshold
    len subarray == k

    1. count
    2. window, avg window, compare to thresh, modify count accordingly
    3. move the window with if statement
"""
        