# Sed
`sed` is used to automate text editing in a script. 

The basics:

```
sed -i 's/regular_expression/replace/g' filename
```

or 

```
sed -i 's/find/replace/' filename
```

`-i` for inplace (e.g., replace and rewrite the file with those changes). Can also be `-i.bak` to have a backup. Unfortunately MacOS requires one, so if you do not want a back up you need to do `-i ''` to essentially say no backup ([source](https://stackoverflow.com/a/5171935)). The `/g` at the very end means that the pattern should be done globally ([source](https://unix.stackexchange.com/a/308519)). By default it will only replace the first one. 

```
sed -i.bak 's/regular_expression/replace/g' filename
```
or

```
sed -i '' 's/regular_expression/replace/g' filename
```

You will eventually run into and issue where you need to replace something that contains a forward slash (`\`). If that happens you can just replace the `/` separating the different parts with literally anything else that is not part of your search or replace query ([source](https://stackoverflow.com/a/7517900)).

```
sed -i 's,regular_expression_containing/forward_slash,replace,g' filename
```
