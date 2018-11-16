Hypothesis Testing & Contrast Analysis

```sas
/* Hypothesis & Contrast Analysis */

TITLE 'Hypothesis & Contrasts';
data pollution;
	infile 'T14_12_POLLUTION.dat' delimiter='09'x;
	input city $ SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip;
run;

PROC GLM;
 CLASS group;
 MODEL SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip = group;
 CONTRAST 'Region  4 vs. Region 1,2 and 3'
 group 1 1 1 -3;
MANOVA H=group/PRINTE PRINTH MSTAT = EXACT;
RUN;

PROC GLM;
 CLASS group;
 MODEL SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip = group;
 CONTRAST 'region 2&3 vs. region 1'
 group -2 1 1 0;
MANOVA H=group/PRINTE PRINTH MSTAT = EXACT;
RUN;

PROC GLM;
 CLASS group;
 MODEL SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip = group;
 CONTRAST 'region 3 vs. region 2'
 group 0 -1 1 0;
MANOVA H=group/PRINTE PRINTH MSTAT = EXACT;
RUN;
PROC GLM;
 CLASS group;
 MODEL SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip = group;
 CONTRAST 'region 1 vs. region 2'
 group 1 -1 0 0;
MANOVA H=group/PRINTE PRINTH MSTAT = EXACT;
RUN;
PROC GLM;
 CLASS group;
 MODEL SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip = group;
 CONTRAST 'region 1 vs. region 3'
 group 1 0 -1 0;
MANOVA H=group/PRINTE PRINTH MSTAT = EXACT;
RUN;
```

Canonical Correlation

```sas
/* Canonical Correlation */

TITLE 'CANONICAL CORRELATION ANALYSIS';
DATA POLLUTION;
	INFILE 'POLLUTION.dat';
	INPUT  city $  Y1 Y2 X1 X2 X3 X4 X5;
  X1X2 = X1 * X2;     X1SQ = X1 * X1;
  X1X3 = X1 * X3;     X2SQ = X2 * X2;
  X1X4 = X1 * X4;     X3SQ = X3 * X3;
  X1X5 = X1 * X5;     X4SQ = X4 * X4;
  X2X3 = X2 * X3;     X5SQ = X5 * X5;
  X2X4 = X2 * X4;     
  X2X5 = X2 * X5;   
  X3X4 = X3 * X4;
  X3X5 = X3 * X5;
  X4X5 = X4 * X5; 
  PROC CANCORR ALL
  VPREFIX = INPUT VNAME = 'INPUT VARIABLES'
  WPREFIX = YIELD WNAME = 'YIELD VARIABLES';
  WITH Y1 Y2 ;
  VAR X1 X2 X3 X4 X5 X1X2 X1X3 X1X4 X1X5 X2X3 X2X4 X2X5 X3X4 X3X5 X4X5 X1SQ X2SQ X3SQ X4SQ X5SQ;
RUN;

```


Principal Component Analysis

```sas
/* Principal Component Analysis */

Title 'PCA';
data pollution;
	infile 'T14_12_POLLUTION.dat' delimiter='09'x;
	input city $ SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip;
run;
proc means data=pollution;
	var SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip;
run;
proc corr data=pollution;
	var SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip; 
run;
proc princomp data=pollution; 
	var SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip; 
run; 
proc princomp cov data=pollution; 
	var SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip; 
run;

```

Factor Analysis

```sas
/* Factor Analysis */

Title 'Factor';
data pollution;
	infile 'T14_12_POLLUTION.dat’;
	input city $ SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip;
run;
proc factor data=pollution
method= principal
priors=smc
nfactors= 3 
rotate= varimax
fuzz=.3 /*deletes factors loadings that are less than .3, so you can see which variables are loading on which factors, this will yield missing values but paint a clearer picture of which variables are loading*/
outstat=stats
plot nplot=2
out=pollution;
var SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip;
run;
proc factor data=pollution
method=principal
priors= 1

rotate= varimax
fuzz= .3; 
var SO2_content Avg_temp No_manufacture Pop Avg_wind avg_precip Avg_daysprecip; 
run; 
proc plot data=pollution; 
plot factor1*factor2; 
run;
```

