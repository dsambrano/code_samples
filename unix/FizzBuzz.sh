#!/bin/bash

test=101
for (( i=1; i<$test; i++ )); do 
if [ $((i%5)) -eq 0 ] && [ $((i%3)) -eq 0 ]
then
echo FizzBuzz 
elif [ $((i%5)) -eq 0 ] 
then 
echo Buzz 
elif [ $((i%3)) -eq 0 ]
then 
echo Fizz 
else 
echo $i 
fi 
done