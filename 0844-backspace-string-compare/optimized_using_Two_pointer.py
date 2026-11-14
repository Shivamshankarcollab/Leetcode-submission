class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first = len(s)-1
        second = len(t)-1
        skip_s = 0
        skip_t = 0
        while first >= 0 or second >=0:
            while first>=0:
                if s[first] == '#':
                    skip_s+=1
                elif skip_s > 0:
                    skip_s-=1
                else:
                    break
                first -=1
            while second>=0:
                if t[second] == '#':
                    skip_t+=1
                elif skip_t > 0:
                    skip_t-=1
                else:
                    break
                second -=1
            if first < 0 and second < 0:
                return True
            if first < 0 or second < 0:
                return False
            if s[first] != t[second]:
                return False
            else:
                first -=1
                second -=1
        return True
            
            



    


        
            
            
        
