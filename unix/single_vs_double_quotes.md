# Single vs Double Quotes

In `bash` single quotes are hard quotes, meaning they only print exactly what is included, so you cannot expand any variables. For that you will need Double quotes. Typically if I need to quote inside quotes I use single then double, but sometimes that wont work because you need to expand a variable. For those situations you can use the `\` escape character. ([source](https://unix.stackexchange.com/a/209972))

```bash
echo '$HOME' # output $HOME
echo "$HOME" # outpue /Users/DSambrano or /home/DSambrano
echo 'EMAIL="example@email.com"' # Quote inside quote
echo "EMAIL=\"$(whoami)@email.com\"" # Quote escaping for variables inside quotes inside quotes

```
