import numpy as np

test = np.array(range(100))+1
mod3 = test%3
mod5 = test%5
final = np.array(test,dtype='a8')
final[(mod3==0) & (mod5==0)] = 'FizzBuzz'
final[mod5==0] = 'Buzz'
final[mod3==0] = 'Fizz'

for i in final:
	print i

	