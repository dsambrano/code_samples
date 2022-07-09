
sims = 100;
stop = 1e7;
CMat = nan(1,sims);
NCMat = nan(1,sims);


for j = 1:sims

    Comment = nan(1,stop);

    tic
    for i = 1:stop
        Comment(i) = toc; % THIS HAS A MEDIUM COMMENT
    end

    Notcomment = nan(1,stop);

    tic
    for i = 1:stop
        Notcomment(i) = toc; 
    end

    CMat(j) = mean(Comment);
    NCMat(j) = mean(Notcomment);
end

mean(CMat)
mean(NCMat)