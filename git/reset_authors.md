# Git Change Authors

Sometimes you might want to change the authorship of a previous commit ([source][]).
If its the most recent commit you can simply do:

```Git
git commit --amend --reset-author --no-edit
```


However, if you are looking to fix a range of commits from the past (say all of them from this computer), then you are looking for this code:

```git
git rebase --interactive --exec "git commit --amend --reset-author --no-edit" {HASH}
```

where `{HASH}` is the commit hash for the start of the range, you wish to edit the authorship of. 
This will create a new file that will automatically go through all of the commits in that range open them change the authorship, rinse and repeat. If there are any conflicts it will have you intereact with the rebase to fix them yourself.

After resolving any errors you can use `git rebase --continue` to indicate that commit has been fixed, `git rebase --skip` to skip that commit, or `git rebase --abort` to abort the rebase process entirely.


[source]: https://jdhao.github.io/2022/08/05/update_commit_author_info_git/
