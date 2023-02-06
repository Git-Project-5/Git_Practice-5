range_num = int(input('Please input range number : '))

def fizzbuzz(n):
  for i in range(1, n+1):
    if i%15 ==0:
      print('FizzBuzz')
    elif i%3==0:
      print('Fizz')
    else:
      print(i)
fizzbuzz(range_num)
