num <- 1000
p <- 1:3/sum(1:3)
cum <- matrix(NaN,1,length(p))
h <- matrix(NaN,1,num)
for(i in 1:length(p)){
  cum[i] <- sum(p[1:i])
}
for(i in 1:length(h)){
  h[i] <- cum*runif(1)
}
hist(h)

# Create Data from abritrary distributions
require(pracma)
x <- c(0, 1, 2, 3); x <- x/sum(x)
y <- cumsum(x)
xi <- runif(20)
yl <- interp1(x = y, y = x, xi)
hist(yl,x)

# Imagesc equivalent
require(RColorBrewer)
require(fields)
require(ggplot2)
hyp1 <- seq(-30,30,.1)
test  <- seq(-30,30,.1)%*%matrix(seq(-30,30,.1),1,601)
image(hyp1,hyp1,test, col = brewer.pal(9,'Greys'))#heat.colors(20,alpha = 1))
# This function does it with the legend
image.plot(hyp1,hyp1, test)
# image.plot(graphics.reset = TRUE)
# Make a color gradient
colfunc <- colorRampPalette(c("white", "black"))
image.plot(hyp1,hyp1, test, col = colfunc(200))
old <- par()
dev.off() # Dev to make sure no futher plots are messed up
cbind(old, par())
