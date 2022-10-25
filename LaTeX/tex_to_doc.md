# Converting LaTeX to Word

Converting your LaTeX documents to word is very commonly needed, if say your collaborators dont use LaTeX or the journal doesnt accept it.
In these scenarios you can use a proprietary solution like:
- Opening the pdf in Microsoft word (best GUI solution) requires internet and Word
- Converting the pdf to .docx with Adobe Acrobat, which of course requires Acrobat.

Both of those solutions are expensive, so one alternative I have found is ([source][]):

```bash
pandoc mydoc.tex --filter pandoc-crossref --bibliography=myref.bib --reference-docx=IEEE_template.doc -o mydoc.docx
```

where `mydoc.tex` is the LaTeX file, `myref.bib` is the bibliography file, IEEE_template.doc is the template/sample file for the journals, and finally `mydoc.docx` is the final document name.

[source]: https://medium.com/@zhelinchen91/how-to-convert-from-latex-to-ms-word-with-pandoc-f2045a762293 "LaTeX to Word"
