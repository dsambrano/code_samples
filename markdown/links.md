# Hyperlinks

Using Hyperlinks in markdown files are super important and super easy. The basic syntaxt is:

```markdown
[visible text](url "title")
```

## Linking Other Files

Linking files are also super easy, you just need to add a single `#` to the beginning of the path. **Note:** Only one single `#` regardless of how many subheaders it is referencing. 

```markdown
[visible text](#pathtofile.md "title")
```

## [Reference Style Links](https://www.markdownguide.org/basic-syntax/#an-example-putting-the-parts-together)

To make things easier to read you can also you reference style [links][1]


```markdown
In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole][1], and that means comfort.

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"

```

## Images

Images follow the same syntax but includes and `!` at the beginning before the square bracket[^2]

```markdown
![alt text](Isolated.png "Title")
```


## Footnotes

Here's a simple footnote,[^3] and here's a longer one.[^bignote]

[1]: https://www.markdownguide.org/basic-syntax/#reference-style-links

[^1]: [SO post](https://stackoverflow.com/a/41912122)

[^2]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
