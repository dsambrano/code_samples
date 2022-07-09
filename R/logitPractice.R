# Sets the Working Directory to the location of this file
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

#Load data
data <- read.csv("logitPracticeData.csv")

#Create plot
plot(data$score.1,data$score.2,col=as.factor(data$label),xlab="Score-1",ylab="Score-2")

#Predictor variables
X <- as.matrix(data[,c(1,2)])

#Add ones to X
X <- cbind(rep(1,nrow(X)),X)

#Response variable
Y <- as.matrix(data$label)


#Sigmoid function
sigmoid <- function(z)
{
    g <- 1/(1+exp(-z))
    return(g)
}


#Cost Function
cost <- function(theta)
{
    m <- nrow(X)
    g <- sigmoid(X%*%theta)
    J <- (1/m)*sum((-Y*log(g)) - ((1-Y)*log(1-g)))
    return(J)
}


#Intial theta
initial_theta <- rep(0,ncol(X))

#Cost at inital theta
cost(initial_theta)


# Derive theta using gradient descent using optim function
theta_optim <- optim(par=initial_theta,fn=cost)

#set theta
(theta <- theta_optim$par)

#cost at optimal value of the theta
theta_optim$value

# probability of admission for student
prob <- sigmoid(t(c(1,45,85))%*%theta)

prob

### Logistic Regression ### With a function
mylogit<- glm(Y ~ X[,2:3], family=binomial(link="logit"))
#printing regression results
summary(mylogit)
#interpreting coefficients as odd-ratios
exp(mylogit$coefficients)

