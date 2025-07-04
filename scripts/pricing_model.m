tbl = readtable('data/processed/loans.parquet');
% Create binary outcome: default=1, paid=0
y = double(strcmp(tbl.status,'Default'));
X = [tbl.rate_offered, tbl.amount];
b = mnrfit(X,y,'model','binomial');
disp('Logistic coefficients:'); disp(b);
% Save coefficients
save('data/processed/logit_coeff.mat','b');
