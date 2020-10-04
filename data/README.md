# Data
Data used to generate paper figures

## time_dist.csv
Number of Patent-Cited and Non-Patent-Cited articles for each year. Used to
generate figure 1b.

## term_freq.csv
Top 100 abstract, title, and MESH terms by frequency over the period 1970-2015
for the Patent-Cited and Non-Patent-Cited corpora. Used to generate figure


## term_ll.csv
Top 30 abstract, title, and MESH terms by log likelihood. Log Likelihood
is calculated according to the formula in "Comparing Corpora using Frequency
Profiling".

## journal.csv
Number of Patent-Cited Articles,	Number of Non-Patent-Cited Articles,
Total Number of Unique Patent Family Citations,	Journal Impact Factor,
and	Patent Impact Factor for all journals and years

## institution.csv
Number of Patent-Cited Articles,	Number of Non-Patent-Cited Articles,
Total Number of Unique Patent Family Citations,	NIH funding,
and	Patent Impact Factor for all institutions and years. NIH funding
acquired from [NIH RePORTER](https://projectreporter.nih.gov/reporter.cfm)

## gender.csv
Number of articles with female/male first/last authors for each year stratified
by corpus

## diversity.csv
Mean and SD of Gini-Simpson index for papers stratified by corpus and year.
Race/Ethnicity determined using the [ethnicolr](https://github.com/appeler/ethnicolr)
python package, which allows for ethnicity determination either using an
algorithm trained on US census data or Wikipedia name data.
Contains value for Gini-Simpson index calculated using the census and
Wikipedia race determination methods. Also includes the Gini-Simpson index
calculated by subsampling 3 random authors for each paper (using census
race determination)
