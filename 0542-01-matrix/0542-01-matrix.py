class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visit = set()
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                mat[r][c] = dist
                for dr, dc in neighbors:
                    row = r + dr
                    col = c + dc
                    if (row < 0 or row >= rows or
                        col < 0 or col >= cols or
                        (row, col) in visit or mat[row][col] == 0):
                        continue
                    queue.append([row, col])
                    visit.add((row, col))
            dist += 1
        return mat


"""
    1. init visit set and queue
    2. loop through grid, append all zeros to queue
    3. init dist
    4. while queue, for all elem in q, write dist to their value
    5. return mat
"""
        