# binary search, add v and v1 to speed up
class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    tmp = [1,4]
    if num in tmp:
      return True
    hi = num
    low = 2
    while hi>low:
      v = int((hi+low)/2)
      v1 = int((hi+low)/2)+1
      if v*v == num or v1*v1 == num:
        return True
      elif v*v > num:
        hi = v
      else:
        low = v+1
    return False


# newton approach
class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    x = num
    while x*x > num:
      x = (x+num/x)//2
    return x*x == num