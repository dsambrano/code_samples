install.packages('BayesFactor')
require(BayesFactor)
data(puzzles)
bf <- anovaBF(RT ~ shape*color + ID, whichRandom = "ID", data = puzzles)
bf

y = rnorm(50)*4 +10
x = .1*y +rnorm(50)
data = data.frame(y,x)
fit = lmBF(y~x, data)
fit
summary(lm(y~x, data))