


# This model assumes that you have data saved in some format that has
# The number probabilities of earning the money, the ambiguity levels
# and the amount of money to be earned. These should be in globally 
# set after the functions are designed but before the optimization is
# called. 
SubjectiveValue <- function(alpha, beta, p, A, V){
    y <- (p - beta * (A/2)) * V^(alpha)
    return(y)
}

cost <- function(theta) {
    alpha <- theta[1]
    beta <- theta[2]
    probs <- data$probs
    ambig <- data$ambig
    vals <- data$vals
    m <- length(y)
    SVfixed <- SubjectiveValue(alpha, beta, rep(1,m), rep(0,m), rep(5,m))
    SVlottery <- SubjectiveValue(alpha, beta, probs, ambig, vals)
    g <- 1/(1 + exp(SVfixed - SVlottery)) # Sigmoid
    p <- (-1/m)*sum((y * log(g)) + ((1-y)*log(1-g))) # Cost function
    return(p)
}

singlePartData <- subset(longformat, longformat$observer == unique(longformat$observer)[1])

y <- singlePartData$choice - 1
params <- 2
data <- singlePartData

#Intial theta
initial_theta <- rep(0,params)

#Cost at inital theta
cost(initial_theta)


# Derive theta using gradient descent using optim function
theta_optim <- optim(par=initial_theta,fn=cost)

#set theta
theta <- theta_optim$par

#cost at optimal value of the theta
theta_optim$value