# Using the `cut` command to remove quotes

You can use the following to remove quotes from a string. You can also replace the double quotes with another character to remove that instead ([source](https://stackoverflow.com/a/35636517))

```bash
TEST=$(echo "here you go"| cut -d '"' -f 2)
```
