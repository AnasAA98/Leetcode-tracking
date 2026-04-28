class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        Left,Right,Und = 0,0,0
        for ch in moves:
            if ch == "L":
                Left+=1
            elif ch == "R":
                Right+=1
            else:
                Und+=1
        return abs(Left - Right) + Und
