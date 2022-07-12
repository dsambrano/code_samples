# Basics
## Normal Mode
When you start up vim you will be in normal mode where you can move around with the arrowkeys or use the vim keys:
- h: left
- j: down
- k: up
- l: right

This will seem a bit strange at first since you can't enter text in this mode, but it has several uses to quickly move around much faster than you could with a mouse. For example, you can move to the beginning of the line you are on with `0` or `^` and you can move to the end of the line with `$`. 

Additionally, you can quickly move down and up with `Ctrl + f` and `Ctrl + b` respectively. 

Want to move to a specific line number? Type `:` then the line number and you will jump there instantly.

Want to jump to a particular word? Type `/` or `?` and the search query. (`/` search forward from cursor and `?` search backwards from cursor position).

What if the text looks a little bland and you want to give it some color? Type `:syntax on`

What if you wanna copy a line, or delete a line, delete everything to the left of your cursor, what about to the right? All of this is possible with as few as twice key presses. 

And this is really just scratching the surface, but basically, vim has a huge learning curve (or shallow curve for my RL folks 😉), but when you learn it, you can move around quite quickly. Much faster than a mouse. Is it worth it for you? I can't answer that, but if you are either a person who loves to maximize efficiency or if you are just a person who like to continue learning knew skill, give it a shot! 

While in normal mode you cannot add text like a typical. To do you you need to enter insert mode

## Insert Mode
You can go to insert mode by typing `i`. If you wanna get fancy, you can even go to insert mode and the beginning of a line (`I`) or the end of a line (`A`). While in insert mode the bottom left of your screen will show `-- INSERT --`.

Now, that you are in Insert mode you can type til your hearts content, but if you want to use any of those shortcuts we talked about you need to exit insert mode with `esc` or you can use my preferred shortcut `Crtl + [`. This will take you back to normal mode, so you can move around the document until you need to enter more text again 😊

## Saving changes and Exiting Vim
Probably the most common thing searched about vim is how to exit/leave vim. Well here you go! First you need to exit insert mode and go to normal mode. If you are already there, great, if not, press the `esc` key or use the shortcut `Crtl + [`.

Now that you are in normal mode you can save changes with `:w` (i.e., write changes) and it should show in the bottom left of the screen, then press enter. You can exit with `:q` and then hit enter or you can do both with `:wq` to save and quit simulatanously.
