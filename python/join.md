# join method

the `.join()` method for strings merges a list of strings into a single string, the initial argument determines what is used to separate out the indexed strings ([source](https://stackoverflow.com/a/12453584)):

```cli
>>> sentence = ['this', 'is', 'a', 'sentence']
>>> '-'.join(sentence)
'this-is-a-sentence'
>>> ' '.join(sentence)
'this is a sentence'
```

