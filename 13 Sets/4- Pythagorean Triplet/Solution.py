def triplets_with_sum(number):
  result = []
  for a in range(1, (number//3)):
      for b in range(a + 1, ((number - a)//2) + 1):
          c = number - a - b
          if a * a + b * b == c * c:
              result.append([a, b, c])
                
    return result
    
