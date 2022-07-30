# Copying and Pasting CLI

There are several solutions out there to solve this problem. My typical one is to use `xclip` to copy use: 

```bash
xclip -sel clip
```

you can also set up a alias to make it shorter. You can ever copy from a file:

```bash
xclip -sel clip < ~/path/to/file.txt
```

And to paste you can use: 

```bash
xclip -o > pastetext.txt
```
One alternative, if you prefer is `pbcopy`:

```
# Linux version of OSX pbcopy and pbpaste.
alias pbcopy=’xsel — clipboard — input’
alias pbpaste=’xsel — clipboard — output’
```
[source][https://medium.com/@codenameyau/how-to-copy-and-paste-in-terminal-c88098b5840d]
