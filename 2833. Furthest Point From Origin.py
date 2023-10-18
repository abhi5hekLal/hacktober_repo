class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_cnt = 0
        r_cnt = 0
        dash_cnt = 0

        for move in moves:
            if move == 'L':
                l_cnt +=1
            elif move == 'R':
                r_cnt +=1
            else:
                dash_cnt +=1
        unified_cnt = 0
        if l_cnt >r_cnt:
            unified_cnt = l_cnt - r_cnt
        elif l_cnt < r_cnt:
            unified_cnt = r_cnt - l_cnt 
        else:
            unified_cnt = 0
        return (unified_cnt + dash_cnt)
