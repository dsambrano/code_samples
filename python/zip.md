# Zip and Unzip

`zip` allows you to take two (or more) lists and create a list of tuples from them where each tuple represents the `ith` element from the lists included ([source](https://realpython.com/python-zip-function/)). 

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zipped  # Holds an iterator object
<zip object at 0x7fa4831153c8>
list(zipped) # returns [(1, 'a'), (2, 'b'), (3, 'c')]
```
Importantly, it returns an iterable object so unless you are combining it with a loop (e.g., `for l, n in zip(letters, numbers): `), you typically want to wrap the output in the `list` function to return a list of tuples.

> **Note**: By defualt the `zip` function will zip until the shortest list is complete. If you want to change that behavior you will need `zip_longest` from the itertools library. 

## Unzip

Unzip allows you to take apart nested lists. Its use the zip function, but you use an asterisk `*` in front of the list to be unziped. Since it is using the `zip` function you usually combine this with the list function to turn it back into a list to be used later.

```python
my_list = [[1,2,3], [4,5,6], [7,8,9]]
list(zip(*my_list)) # Returns a new list of tuples: [(1,4,7), (2,5,8), (3,6,9)]
```

Now the elements are organized based on their sublist index ([source](https://stackoverflow.com/a/52194683)). 
