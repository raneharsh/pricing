libname in parquet 'data/processed/loans.parquet';
proc means data=in.loans n nmiss;
  var amount rate_offered;
run;
