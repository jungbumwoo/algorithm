class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_stack_cnt = 0
        d_stack_cnt = 0

        r_cnt, d_cnt = senate.count("R"), senate.count("D")
        have_rights = [True] * len(senate)

        index = 0

        while True:
            
            s = senate[index]
            
            if r_cnt == 0:
                return "Dire"
            if d_cnt == 0:
                return "Radiant"
            
            if have_rights[index] is False:
                index += 1
                index %= len(senate)
                continue

            if s == "R":
                if d_stack_cnt > 0:
                    d_stack_cnt -= 1
                    r_cnt -= 1
                    have_rights[index] = False
                else:
                    r_stack_cnt += 1
            
            elif s == "D":
                if r_stack_cnt > 0:
                    r_stack_cnt -= 1
                    d_cnt -= 1
                    have_rights[index] = False
                else:
                    d_stack_cnt += 1

            index += 1
            index %= len(senate)
