# Bash Try Catch

Unfortunately, `Bash` does not natively have any try catch but it can be emulated ([source](https://stackoverflow.com/a/22010339))

```bash
{ # try

    command1 &&
    #save your output

} || { # catch
    # save log for exception 
}
```

This takes use of the `||` and the `&&` operators. The former runs the second command if the first fails, while the latter runs only if the first command succeeds. They are then wraped in curly braces to group setups of commands
