# Multiple files

Dealing with multiple files is how you can really turn vim into a proper IDE.
First, I do recommend when dealing with a project to open the project folder in vim instead of a particularly file `vim .`
But once you are in a file, you will likely need to edit another.
To do so, you just need to use the `:e file-or-dirname` and of course tab completion works here as well.
This will open that file in a new buffer. 

A new buffer allows you to make all the changes you need and then you can use `:bnext` and `:bprevious` to move between them. 
What is nice, is it will same your position in each file as well. 
But of course sometimes you will have to many files open and it will be tedious to cycle through them all. 
In those case, you can check you buffers with `:buffers` or `:ls` and then close them with `:bd#` or just close the current one with `:bd`.
And of course tab completion also works here.
> **Note**: Once a file is in the list of buffers you can't tab complete to edit it, so you should be using `:bnext` or better yet, remap them both. 


[source](https://vi.stackexchange.com/a/3067)
