# Find Hash

You can get the hash of a commit with `git log`, but if you need it for a branch you can use:

```bash
git re-parse BRANCH_NAME
```
Prepending `origin/` to the `BRANCH_NAME` will track remote ones as well ([source][]).

[source]: https://stackoverflow.com/a/9110527
