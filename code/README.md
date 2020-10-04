# Code

## clean.py
Methods to clean Non-Patent-Literature citations for patents

## query.py
Reference consolidation involved the use of (GROBID)[https://github.com/kermitt2/grobid]
and (biblio-glutton)[https://github.com/kermitt2/biblio-glutton]. This is the
query sent to the GROBID server for reference consolidation. See supplemental
methods for more details about reference consolidation methods.

## gender.R
Method to determine author gender from first name using R (gender)[https://github.com/ropensci/gender]
package

## model.py
Logistic regression model to predict patent-citation status from TF-IDF
encoded article abstract. Splits paper dataset into training and test set
80%/20% respectively. Trains TF-IDF vectorizer, performs training as well as
test set prediction.
