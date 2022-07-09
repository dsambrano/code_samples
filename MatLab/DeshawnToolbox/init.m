function [ olddir, newdir] = init()
%This function initializes a script by clear all; close all; clc; and
%sets your path as to current file path.
%   Deshawn Sambrano: DSambrano@nyu.edu
   %Version 1: 9-15-17
    close all; clear all; clc

    % Set working directory to this file because I am lazy.
    olddir = pwd;
    tmp = matlab.desktop.editor.getActive;
    newdir = fileparts(tmp.Filename)
    cd(newdir);

end

