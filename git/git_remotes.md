# Setting Get Remotes

When you make a new local branch you often need to push it to a remote.
The easiest way to do that is by using get push ([source](https://stackoverflow.com/a/1519032)):

```
git push <remote-name> <local-branch-name>:<remote-branch-name>
```

however, in most contexts you will want to maintain that connection so that this branch will always link to that remote branch. In which case you will want to add the `--set-upstream` option. For example:

```
git push --set-upstream origin dev

```

