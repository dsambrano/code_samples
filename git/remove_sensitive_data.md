# Remove Sensitive Data

Sometimes you accidentally include sensitive data like API key, or a password, etc. and you need to remove it from your git repo. The problem is anyone who views the history can still see it. So the solution is to [rewrite history](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). There are two methods, the traditional [`git-filter`](https://git-scm.com/docs/git-filter-branch) command and the open source [`BFG Repo-Cleaner`](https://rtyley.github.io/bfg-repo-cleaner/) the former being built into git and the later being an open source alternative that is faster and simplier. 

## BFG Repo-Cleaner

Use you favorite package manager to install or download at the [link](https://rtyley.github.io/bfg-repo-cleaner/). My preferred method is to have a `passwords.txt` file the specify what to do with what text. But you can also [delete specific files](https://rtyley.github.io/bfg-repo-cleaner/#examples) if that is more suited to your scenario. To delete with a `passwords.txt` file, you just need to have a clean repo and use the following command. One super important note about this, is it only removes your history, to properly remove you

```
bfg --replace-text passwords.txt  my-repo.git
```

One super important note about this, is that it only removes these data from your history. To properly remove them you will still need to remove it from the head and then do a forced push to the remote repo. This will mess up everyones pushes and merges, so make sure every one pushes their changes first and you merge all pull requests before doing this.  

[Example](https://gist.github.com/w0rd-driven/60779ad557d9fd86331734f01c0f69f0) `passwords.txt` file. 

```
PASSWORD1                       # Replace literal string 'PASSWORD1' with '***REMOVED***' (default)
PASSWORD2==>examplePass         # replace with 'examplePass' instead
PASSWORD3==>                    # replace with the empty string
regex:password=\w+==>password=  # Replace, using a regex
regex:\r(\n)==>$1               # Replace Windows newlines with Unix newlines
```
