# Inserting Text at the beginning (or end) or multiple lines

All commands assume normal mode. [Source](https://techglimpse.com/insert-text-beginning-line-vim/)

Lets say you need to add the word alias to the front of multiple lines You can do that with the following

```
:%s/^/alias
```
if you only want some of the lines, like lines 10-20 you can use this command:

```
:10,20s/^/alias 
```

when you want to replace something with a new line use the `\r` instead of the standard `\n` [source](https://stackoverflow.com/a/71334)

```
s#\. #. \r#g
```
