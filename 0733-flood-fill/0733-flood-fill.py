class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
            1. start at sr, sc, save original color
            2. check all adjacent neighbours and modify
            3. recursively check all neighbouring
        """
        ROWS, COLS = len(image), len(image[0])
        orig = image[sr][sc]
        visit = set()

        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visit or image[r][c] != orig:
                return

            image[r][c] = color
            visit.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)

        return image
            

        