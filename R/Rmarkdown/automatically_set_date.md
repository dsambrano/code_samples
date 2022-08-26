# Automatically set the date

Setting the date automatically so that it will change was your re run your script. ([source](https://bookdown.org/yihui/rmarkdown-cookbook/update-date.html))


```R
date: "`r format(Sys.time(), '%B %d, %Y')`"
```
