# Pathlib

As of 3.5+ the modern solution to getting a path variable in python is with the pathlib library. 

```python
from pathlib import Path
FILENAME = Path.home() / Path('Library/Application Support/Code/User/setting.json')
```

As you can see in the example above you can seemlessly combine paths together.
Not shown is is the advantage of a much more OOP/pythonic syntax with things like

```python
file = Path(my_file.text)
file.exists()
file.is_file()
file.is_dir()
file.open()
file.close()
```
So not quite a drop in replacement for os.path, but with a little tweeking it will make all the difference.
