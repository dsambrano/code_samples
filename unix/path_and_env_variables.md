# Path and other Env(vironment) Variables

## Path

Updating your `PATH` variable is extremely common to allow you to use scripts anywhere ([source](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)). 

```
export PATH="directory/to/add:$PATH"
```

You can also flip `$PATH` and `directory/to/add` to add it to the end of you path.

## Env(ironment) Variables

The `PATH` is just one environment variable, but you have others. 
They can all be listed out with `env`. 
Some common ones are `HOME` which is used to allow the shortcut `cd ~` and always get you to your home directory. 
The useful thing is that you can store `ENV` variables that can be used in your programs. 
This is super common in python and there is a whole package ([dotenv](https://pypi.org/project/python-dotenv/). 
Other languages have similar mechanisms. 
The `ENV` is used to make consistent development environments and store secret/protected information. 

