# Excluding Files

Sometime you need to exclude files in `git`, if its only 1 or 2 its easy to work around or to restore them after adding everything, but if there is a lot, that solution sucks.
Instead check out this from [Stackoverflow][source]:

```
git add -- . ':!path/to/file1' ':!path/to/file2' ':!path/to/folder1/*'
```



[source]: https://stackoverflow.com/a/51914162

