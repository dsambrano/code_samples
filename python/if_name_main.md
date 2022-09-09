# If Name Main

You have probably seen this a bunch of times, but what does it actually mean:

```python
if __name__ == '__main__':
    main()
```

All that this is saying is that this script will check if you ran it as the main file.
In other words you can it through the terminal and this file wasn't imported in from another file.
This helps keep code more organized, by only running things automatically if it is the main file, but not if it is an imported file/module. 
It is good practice to do this on all your scripts
