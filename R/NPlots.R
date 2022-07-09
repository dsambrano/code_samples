# , knitr=isTRUE(getOption('knitr.in.progess')) Testing if its being knitted
nplots <- function(data, ivs=NULL) {
  vars <- names(data)
  if (is.null(vars)) {
    vars <- "data"
    data <- matrix(dv, length(dv), 1)
  }
  old <- par()$mfrow
  on.exit(par(mfrow = old), add = TRUE)
  for(i in 1:length(vars)){
    if(is.factor(data[,i])) {
      par(mfrow = c(1,1))
      tab = table(data[, i])
      barplot(main = vars[i], tab, col = c(2:(length(tab)+1)))
    }
    else{
      if(!is.null(ivs)){
        for(k in 1:length(ivs)){
          for(j in 1:length(levels(ivs[[k]]))){
          dataset <-subset(data, ivs[[k]] == levels(ivs[[k]])[j])
          par(mfrow=c(2,2))
          hist(dataset[, i], main = paste(vars[i]," + \n",levels(ivs[[k]])[j]), xlab = "")
          qqnorm(dataset[, i], col = "red", main = 
                   paste(vars[i]," + \n",levels(ivs[[k]])[j]))
          qqline(dataset[, i])
          plot(density(na.omit(dataset[, i])), ylab="Proportjon", main = 
                 paste(vars[i]," + \n",levels(ivs[[k]])[j]))
          polygon(density(na.omit(dataset[, i])), col = "cyan")
          boxplot(dataset[, j], main = paste(vars[i]," + \n",levels(ivs[[k]])[j]))
          }
        }
      }
      else{
        par(mfrow=c(2,2))
        hist(data[, i], main = vars[i], xlab = "")
        qqnorm(data[, i], col = "red", main = vars[i])
        qqline(data[, i])
        plot(density(na.omit(data[, i])), ylab="Proportion", main = vars[i])
        polygon(density(na.omit(data[, i])), col = "cyan")
        boxplot(data[, i], main = vars[i])
      }
    }
  }
}