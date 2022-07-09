library(rgl)
plot3d(iris[,2:4])



library(geoR)
elevation.df = data.frame(x = 50 * elevation$coords[,"x"],y = 50 * elevation$coords[,"y"], z = 10 * elevation$data)
elevation.loess = loess(z ~ x*y, data = elevation.df, degree = 2, span = .25)
elevation.fit = expand.grid(list(x = seq(10, 300, 5), y = seq(10, 300, 5)))
z = predict(elevation.loess, newdata = elevation.fit)
elevation.fit$Height = as.numeric(z)


persp(seq(10, 300, 5), seq(10, 300, 5), z, phi = 45, theta = 45,
      xlab = "X Coordinate (feet)", ylab = "Y Coordinate (feet)",
      main = "Surface elevation data"
)