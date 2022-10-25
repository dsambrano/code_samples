# MD

Making a Directory and then immediately `cd`ing into that dir is super common. 
Here is a one liner that will do it for you.
You can make it an function and add it to your path for extra benefits.

```bash
mkdir test && cd $_
```

if you want to make dir and vim into the file you can use:

```bash
mkdir test && vim "$_"/file_name
```
