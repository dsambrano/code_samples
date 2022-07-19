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

