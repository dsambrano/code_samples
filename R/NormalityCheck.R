####Normality check all plots on one screen
vars <- names(data)
for(i in 1:ncol(data)){
  par(mfrow=c(2,2))
  hist(data[,i], main=vars[i])
  qqnorm(data[,i], col="red", main=vars[i])
  qqline(data[,i])
  plot(density(na.omit(data[,i])),ylab="Proportion",main=vars[i])
  polygon(density(na.omit(data[,i])),col="cyan")
  boxplot(data[,i], main=vars[i])
}