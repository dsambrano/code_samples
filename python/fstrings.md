# f strings

f strings are the modern python implementation for formating string.

One super neat trick is you can use them to ensure a string is a certain length ([source](https://youtu.be/dvqFNOhNIjM))

```python
greet="hi"
f"{greet:_^10}"
```

this makes the text hi surrounded by `_` such that the whole this is 10 characters long. If you want a different character replace the `_` or put nothing for a space. The `^` can be replace with a `>` or `<` to make the text flush right and left respectively.


```python
num = 1_000_000
print(num) # Output: 1000000
f"{num:,} # Output: 1,000,000
```

f strings can also be used to round [values](https://stackoverflow.com/a/50340297)


```python
f'{value:{width}.{precision}}'
```

where:

- `value` is any expression that evaluates to a number
- `width` specifies the number of characters used in total to display, but if value needs more space than the width specifies then the additional space is used.
- `precision` indicates the number of characters used after the decimal point

Additional info about fstrings can be found [here][https://realpython.com/python-f-strings/]
