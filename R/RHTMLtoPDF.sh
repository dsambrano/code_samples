#!/bin/bash

# Must be in directory

input=$1
filename=$(basename "$input")
#filename="${filename%.*}"
# RMD=rmarkdown::render\(${input}\)
#now="$(echo Rscript -e rmarkdown::render\(\"$filename\"\))"
# V2=$(dirname "${input}")
# repo=$(pwd)

# if [ V2 = "." ]
# then
#       echo "true"
#       repo=$(pwd)
# else
#       echo "false"
#       repo=$V2
# fi






cp -r ./ ~/Desktop/HTMLtoPDFtemp/

Rscript ~/Documents/Hacks/ChangeSegue.R $(pwd) 








#cd $repo







#echo "Rscript -e $RMD"

#Rscript -e rmarkdown::render('NYUTheme.Rmd')
# RMD=rmarkdown::render\(${input}\)

# echo $1

# echo "Rscript -e $RMD"