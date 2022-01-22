"""
Given a string as input, convert all the alphabets in it to lowercase.
Input-> "Hello"
Output-> hello
"""

st = "Hello"
ln = len(st)
for i in range(0,ln):
  e = st[i]
  if(e>="A" and e<="Z"):
    e = e>="a" and e<="z"
    st[i] = e
print(st)
