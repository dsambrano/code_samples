# Case Switch in Bash #

Often times you need to either assign a variable depending on another or run slightly different code depedning on another variable.
Instead of running several `if` statements, you can just use a `case` statment.

Here is the basic strucutre:

```bash
OS="MacOS"
case $OS in
  *"Mac"*)
    echo "Apple";;
  "linux")
    echo "Linux";;
  *"windows"*)
    echo "Gross";;
  *)
    echo "Unknown OS";;
esac
```

> Note how I used `*` as a wildcard to indicate if `Mac` is anywhere in the string.

If the string contains `Mac` then the lines under it will run otherwise it will check if it contains `linux` to run those lines.
Finally, it checks it if there is any text at all, in which case it now states unknown.

[source]: https://linuxize.com/post/bash-case-statement/ "Case Statement"
