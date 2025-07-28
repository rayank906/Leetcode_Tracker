class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()

        queue.append(0), visited.add(0)

        while queue:
            room_idx = queue.popleft()
            visited.add(room_idx)
            for key in rooms[room_idx]:
                if key not in visited:
                    queue.append(key)
        return len(visited) == len(rooms)


"""
    1. make a set of visited keys
    2. create a queue for rooms to visit
    3. init set and key with 0 as first element
    4. while queue
        pop room_idx and add to visit
        for every key in room, check if key was visited
            if not visited, add to queue
    5. return len(set) == len(rooms)

    TimeC: O(n * m), where m is number of keys
    SpaceC: O(k), where k is the number of keys present
"""
        