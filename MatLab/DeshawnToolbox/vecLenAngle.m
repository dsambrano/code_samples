function [theta, LenA, LenB] = vecLenAngle( A, B )
%Returns vector lengths and the angle between two vectors
%   This function provides a useful way to extract the vector length of two
%   vectors along with the angle between to vectors IN DEGREES.
%   Deshawn Chatman Sambrano: DSambrano@nyu.edu
%   Version 1: 9/11/17
    LenA = sqrt(sum(A.^2));
    LenB = sqrt(sum(B.^2));
    if LenA == 0
        error('The first vector has a L^2 norm of 0: Process ended')
    elseif LenB == 0
        error('The second vector has a L^2 norm of 0: Process ended')
    end
    if length(A) > 2 | length(B) > 2
        warning('At least one of your vectors have a vector dimensionality of more than 2. Thus, theta may not make sense in this case')
    end
    theta = rad2deg(acos(dot(A,B)./(LenA.*LenB)));
end

