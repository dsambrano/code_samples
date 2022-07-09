set.seed(50)
y = rnorm(50, 0, 1)
x = y*.8 + rnorm(50, 0, 1)
cor(x,y)
n = resid(lm(y~x))*.33 + rnorm(50, 0, 1)
# As shown this is not related to the variable itself
summary(lm(y~n))
# Only to the error term
summary(lm(resid(lm(y~x)) ~ n))
# However as a consequence that means that it magically related in multiple regression
summary(lm(y~n+x))