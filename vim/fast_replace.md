# Fast Replace

You can do some really fast replacing with the `s` command to use regex.
One simple example is with the following.
Pretend you need to edit this block of text:

```
{
  ^c = copy:;
  ^x = cut:;
  ^v = paste:;
}
```

If you want to change them to have the part before the `=` you can use visual mode to select all those lines then hit `:` to enter into command mode and type in:

```
s/\(\^.\)/"\1"
```
This will select the first `^` plus one character after that.
Now here is the neat trick. 
The `"\1"` says replace the thing grabbed in the first part with itself surrounded by double quotes.

Just in case you didn't get that, let's finish this example by encompassing the right side in double quotes as well (excluding the `;`).
This will again be done by using visual mode to select the lines then entering command mode.
This time you will enter the following:

```
s/= \(\w.*:\)/= "\1"
```

This will grab the world following the `=` and a space.
However, it will only go up to the `:` and not to the `;`
Using the same strategy, you can then replace the collected word with itself surrounded by double quotes.
This is a super useful technique because each block of text was a different size so we specifically need to allow it to be variable sized. 


[source](https://youtu.be/uL9oOZStezw?t=514)
