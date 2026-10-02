def combo(s):
  i = 0
  combos=[]
  print(len(s)-1)
  for i in range(0,len(s)):
    num = s.index(i)
    j = s[num] + s[num-1] + s[0]
    return j 
    
