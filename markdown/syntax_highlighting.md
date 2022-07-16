# Syntax highlighting

Have nice color syntax is a important part of markdown. However, sometimes markdown does not correctly highlight your code. You can force it to use the correct highlighting by telling markdown. For example:

````

```language
```

````

where language can be pretty much any common language you can think of. If you want to check if yours works, you can view this [link](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml), which is specific to github style. Other styles (e.g., R markdown) may have slightly different ones. That said, I do want to points out a few that would be helpful:

- python (obvious)
- R (obvious)
- shell, bash, zsh (for shell languages)
- console (my new favorite which lets you highlight if you are mimicing a console as opposed to just a shell [source](https://stackoverflow.com/a/49004070))
