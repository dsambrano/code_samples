
draws <- 10000
data <- matrix(0,draws,2)
for (i in 1:draws){
mu <- c(10, 0)
p <- length(mu)
Sigma <- matrix(c(1,.2,.2,1),2,byrow = TRUE)
eS <- eigen(Sigma, symmetric = TRUE)
ev <- eS$values
n <- 1
X <- matrix(rnorm(p * n), n)



X <- drop(mu) + eS$vectors %*% diag(sqrt(pmax(ev, 0)), p) %*% t(X)
data[i,] <- X
}

colMeans(data)
cor(data)
plot(data)
