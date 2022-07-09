function [ L2 ] = vecLen( A )
%This function gives the vector length/L^2 norm/Euclidian space/magnitude of a vector
%   Deshawn Sambrano: DSambrano@nyu.edu
%   Version 1: Sept 21 2017
       
    L2 = sqrt(sum(A.^2));

end

