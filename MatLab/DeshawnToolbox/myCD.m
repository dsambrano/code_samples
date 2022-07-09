function [ olddir, newdir ] = myCD( )
%Set current working directory as the dir for this file
%   Deshawn Sambrano: DSambrano@nyu.edu
   %Version 1: 9-15-17
    olddir = pwd;
    tmp = matlab.desktop.editor.getActive;
    newdir = fileparts(tmp.Filename)
    cd(newdir);
end

