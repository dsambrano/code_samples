## Basic Tutorial
# https://cran.r-project.org/web/packages/reticulate/vignettes/calling_python.html

# install.packages("reticulate") # N
library(reticulate)
os <- import("os")
sys <- import("sys")
sys$version
sys$path
pd <- import('pandas')
np <- import('numpy')
scipy <- import('scipy')

py_run_string("x = 10")

# access the python main module via the 'py' object
py$x

# import numpy and specify no automatic Python to R conversion
np <- import("numpy", convert = FALSE)

# do some array manipulations with NumPy
a <- np$array(c(1:4))
sum <- a$cumsum()  # This would not work with automatic conversion

# convert to R explicitly at the end
py_to_r(sum)

py_help(os$chdir)

