from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        R, C = len(board), len(board[0])
        q = deque()

        def add(r, c):
            if board[r][c] == "O":
                board[r][c] = "T"   # mark when enqueuing to avoid duplicates
                q.append((r, c))

        for c in range(C):
            add(0, c)
            add(R - 1, c)
        for r in range(R):
            add(r, 0)
            add(r, C - 1)

        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    q.append((nr, nc))

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

