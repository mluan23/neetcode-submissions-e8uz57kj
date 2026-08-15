class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we want O(n^2)
        # so you can do 2 x 3 nested for loops technically?
        # basically all you need to check, at least for r and c
        # is just if there is no dupes
        # so just use a set for each, and if already seen not valid
        # so at least for r and c is not too bad
        # so you could do nested for loop, one for r and c
        # we handle r and c first because they are simpler

        # ok now to do the box
        # you can use those sorta row and col tricks
        # you just need to keep track of your box sorta
        # so using r,c you can determine the box right?
        # ok so you just need another 9 sets for each box
        # ah you can track your box using r,c right and map to sets
        def get_box(r,c):
            box_r = r // 3
            box_c = c // 3
            box = box_r * 3 + box_c
            return box
        c_sets = dict()
        box_sets = dict()
        for i in range(9):
            c_sets[i] = set()
            box_sets[i] = set()
        for r in range(9):
            r_set = set()
            for c in range(9):
                entry = board[r][c]
                if entry == '.':
                    continue
                if entry in r_set:
                    return False
                r_set.add(entry)
                if entry in c_sets[c]:
                    # print(entry,r,c,c_sets[r])
                    return False
                c_sets[c].add(entry)
                if entry in box_sets[get_box(r,c)]:
                    return False
                box_sets[get_box(r,c)].add(entry)
        return True
        
