function [ samllestDimension ] = width( inputArray )
% width: This function determines and outputs the smallest dimension of the input array
%   Deshawn Sambrano: DSambrano@nyu.edu
%   Done in 2017
B = rand(10,5); % This will not be output to the workspace\
C = rand(9,4);

smallestDimension = min(size(inputArray));

temp1 = nan(1,4);
temp2 = nan(10,1)
C = [C; temp1];
C = [C  temp2];


temp = B + C; % This will throw and error to debug a funtion you have to set a breakpoint

disp('Function Complete, executed without errors')
% load handel % This might be a bit much
% sound(y, Fs) 

end

