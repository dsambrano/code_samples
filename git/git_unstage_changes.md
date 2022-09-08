# Unstage Changes

To unstage changes look no further than the `git reset` command. You can do it on a file:

```bash
git reset file_name
```

or you can do it on everything thing in the repo:

```bash
git reset .
```

Newer versions of `git` (after 2.24) allow you to use `git restore --staged` ([source]**(https://stackoverflow.com/a/6919257))
