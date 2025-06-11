class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1:
                if flowerbed[0] == 0:
                    count +=1
                break
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    count += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
        if n <= count:
            return True
        return False
        