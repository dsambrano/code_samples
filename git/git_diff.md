# Diff 

You can use the diff command to see what has change since last commit, if you havent already staged the changes.

But ifyou want to see what was different between older ones, you need: 

```bash
git diff hash..hash
```

Removing the `..` just looks at the two and adding it in looks at all consecutive ones([source][]).


If you are looking to get the difference between the last commit and the staged data you can use ([cached-diff][]):

```bash
git diff --cached
```


[source]: https://stackoverflow.com/a/3368758
[cached-diff]: https://stackoverflow.com/a/1587877 "Cached Diff"
