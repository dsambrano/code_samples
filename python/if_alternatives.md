# If Statement Alternatives

If you are looking to improve your code, you will see tons of blog posts and YouTube videos telling you why you should never use IF/Else statements. While that is definitely an over exaggeration, there are many cases where you can use an alternative that makes your code both more readable and more maintainable. Below are some examples ([source](https://medium.com/swlh/3-alternatives-to-if-statements-to-make-your-python-code-more-readable-91a9991fb353)):

Replace:

```python
if user == "approved" or user == "good" or user == "Yeup"
    give_access()
```

with:

```python
allow_types = ["approved", "good", "Yeup"]
if user in allow_types:
    give_access()
```

Another option is to use dictionarys. So you would replace

```python
def show_info(choose_item="phone"):
  if chosen_item == "phone":
    return "Handheld communication device"
  elif chosen_item == "car":
    return "Self-propelled ground vehicle"
  elif chosen_item == "dinosaur":
    return "Extinct lizard"
  else:
    return "No info available"
```

with:

```python

def show_info(chosen_item="phone"):
  info_dict = {
    "phone": "Handheld communication device",
    "car": "Self-propelled ground vehicle",
    "dinosaur": "Extinct lizard"
  }

  return info_dict.get(chosen_item, "No info available")
```

> **Note**: The `.get()` method to set a default if they key is not in the dictionary. Alternatively you can have everything in one line, if you don't assign the dictionary, but just use the `.get()` methond on the `{}` in the return line. E.g., `return {"phone": "yes"}.get(x, "Not Available")` ([source](https://stackoverflow.com/a/103081))

This even works with functions ([source](https://stackoverflow.com/a/60215)):

```python
def multi_func(value -> str):

    result = {
      'a': lambda x: x * 5,
      'b': lambda x: x + 7,
      'c': lambda x: x - 2
    }[value](x)
    return result
```

> **Note**: This uses anonymous functions here, but they could also use named functions aswell see this [example](https://medium.com/swlh/3-alternatives-to-if-statements-to-make-your-python-code-more-readable-91a9991fb353#6a88)
