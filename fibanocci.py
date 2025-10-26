print(0)
print(1)

count = 2

def fibanocci(previous_one, previous_two):
  global count
  if count <= 19:
    new_fibanocci = previous_one + previous_two
    print(new_fibanocci)
    previous_two = previous_one
    previous_one = new_fibanocci
    count+=1
    fibanocci(previous_one, previous_two)
  else:
    return
  

fibanocci(1, 0 )