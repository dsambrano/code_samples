#!/bin/bash

input=$1
output=${input%.pdf}.png
color=$2

convert -density 300 -depth 8 -quality 95 $input $output
convert $output -fuzz 20% -transparent white $output 


if [ -z "$2" ]
then
      echo "Conversion Complete"
else
	  convert $output -fuzz 20% -fill $color -opaque "#000000" $output
      echo "Conversion Complete and all black was changed to $color"
fi
