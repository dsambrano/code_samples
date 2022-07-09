# Obtained from: http://adv-r.had.co.nz/Performance.html


require(microbenchmark)
nsamples <- 1000000
m <- 8
y <- sample(0:1,8, replace = TRUE)
h <- runif(8,0,1)
microbenchmark(
    (-1/m)*((y)%*%log(h)+((1-y)%*%log(1-h))),
    (-1/m)*sum(((y)*log(h)+((1-y)*log(1-h)))), times=nsamples
)
