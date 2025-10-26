print(0)
print(1)

count = 2

def fibonacci(previous_one, previous_two):
  global count
  if count <= 19:
    new_fibonacci = previous_one + previous_two
    print(new_fibonacci)
    previous_two = previous_one
    previous_one = new_fibonacci
    count+=1
    fibonacci(previous_one, previous_two)
  else:
    return
  

fibonacci(1, 0 )