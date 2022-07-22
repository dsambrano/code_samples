# View changed values since last X commits

```
git log -1 --name-only --oneline # Replace -1 with whichever number is valuable
```

[source][https://stackoverflow.com/a/49854849]

## Specific files history

```
g log --follow --stat -p file
```

[source](https://kgrz.io/use-git-log-follow-for-file-history.html)
