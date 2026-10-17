class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
            - init res matrix w r:c, c:r
            - loop through matrix w r,c
            - put r,c at c,r
            - return res
            TC: O(mxn), O(mxn)
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0 for i in range(ROWS)] for i in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
        return res
        