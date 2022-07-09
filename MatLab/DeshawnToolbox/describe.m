function [ Mat ] = describe( A )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    
    
    ncol = size(A,2);

    
%     Mat = nan(ncol,7); 
    %  vars n  mean sd median trimmed mad   min   max range skew kurtosis se
    if istable(A)
        vars = A.Properties.VariableNames';
        A = table2array(A);
    else
        vars = 1:ncol;
    end
    
    Mat = table(vars', ncol-sum(isnan(A))', sum(isnan(A))', nanmean(A)',... 
        nanstd(A)', nanmedian(A)', mad(A,1)', kurtosis(A)', skewness(A)', ...
        (nanstd(A)./sqrt(ncol-sum(isnan(A))))');
    Mat.Properties.VariableNames = {'Vars','N','Missing','Mean' 'SD', ...
                                    'Median', 'MAD', 'Kurtosis', ...
                                    'Skewness', 'SE'};
end

