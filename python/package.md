# Installing a Local Package

Installing a Local Package has many use cases, which I will not cover here, but it is really simple.
First you need to make a package.
For that all you need is the have a `__init__.py` file in the folder.
You can place any extra modules next to it and any necessary functions inside this file, but it can be empty.

Next in the parent directory you need to make a `setup.py` file which contains:

```python
from distutils.core import setup

setup(name='PACKAGE_NAME', version='1.0.0', packages=['PACKAGE_NAME'])
```

of course replaceing `PACKAGE_NAME`.
The full strucutre would look something like the following:


```bash
rice
├── rice
│   ├── change_alacritty_theme.py
│   ├── change_wallpaper.py
│   ├── __init__.py
│   └── run.py
└── setup.py
```

Finally, you just need to install that package with:

```python
python3 -m pip install -e PATH/TO/PACKAGE
```

of course replacing `PATH/TO/PACKAGE` with the location of the package.
This is the direcory containing the `setup.py` file not the `__init__.py` file.

[stackOF]: https://stackoverflow.com/questions/42494229/how-to-pip-install-a-local-python-package
