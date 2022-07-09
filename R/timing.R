library(tictoc)
library(beepr)
tic()
Sys.sleep(3)
toc()
alarm()
beep(10)
system("say Just finished!")


for(i in 1:12){
  beep(i)
  Sys.sleep(2)
}
  
  
