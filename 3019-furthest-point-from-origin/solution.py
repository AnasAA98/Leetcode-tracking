class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L,R,U = 0,0,0
        for c in moves:
            if c == "L":
                L +=1
            elif c == "R":
                R += 1
            else:
                U += 1
        return abs(L - R) + U
