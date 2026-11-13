class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t= list(t)
        i = 0
        j= 0
        while i<len(s):
            if s[i] == '#':
                if i == 0:
                    s.pop(i)
                else:
                    s.pop(i-1)
                    s.pop(i-1)
                    i -=1
            else:
                i+=1

        while j < len(t):
            if t[j] == '#':
                if j == 0:
                    t.pop(j)
                else:
                    t.pop(j-1)
                    t.pop(j-1)
                    j-=1
            else:
                j+=1
        if s==t:
            return True
        else:
            return False

            
            
        
