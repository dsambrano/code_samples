#!/usr/bin/env bash

# Requests user input
read -p "Would you like to install GUI apps installed or is this a server only: [server]/gui/all: " GUI
GUI=${GUI:-server} # Sets default (if nothing is typed in) to server

echo $GUI # Prints out as proof
