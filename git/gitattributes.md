# Git Attributes
If you ever work across Unix like OS (e.g., MacOS and Linux) and windows you might get a warning saying something like the following:

```
warning: converting crlf to lf 
```

which may seem pretty concerning, but it just means that they converting the new line characters to match the appropriate ones for unix like OSes (see this [post](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/#the-old-system) or this [SO answer](https://stackoverflow.com/q/3206843) for more details). Even if its not super concerning it can be quite annoying. 

The old solution to dealing with this problem is to set your global config to `core.autocrlf = input` with:

```
git config --global core.autocrlf input # For Unix like OS 
git config --global core.autocrlf true # For windows 
```

The more modern solution is to use a `.gitattributes` file. This is the preferred method because you don't have to worry about whether everyone/computer has set their proper setting for the project. Instead you specific which files should be change to which settings and which should not. 

A simple, but not necessarily optimal solution is to use include the following as the first line in the `.gitattributes`

```
*       text=auto
```

but for more detailed info see this [post](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/#the-new-system). There is also a [SO post](https://stackoverflow.com/a/10855862) that has a sample file. 

