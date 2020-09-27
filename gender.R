"""
File: gender.R

Function utilizes the gender R package to detemine the gender for all first names in a dataframe.
"""
library(gender)
library(tidyverse)

get_gender <- function(df, var) {
  """
  Params:
    df - dataframe containing as columns var and pmid (pmid for each paper)
    var - name of the column in the data frame containing the first names to be 
  """
  gender <- df %>% select(pmid, all_of(var), year) %>% mutate(min_year=year-75, max_year=year-15)
  gender$min_year <- pmax(1880, pmin(gender$min_year, 2012))
  gender$max_year <- pmax(1880, pmin(gender$max_year, 2012))
  
  # Removes most first names that are initials
  first <- gender %>% filter(nchar(gender[,var]) > 1)
  
  output <- gender_df(first, name_col=var, year_col=c("min_year", "max_year"))
  output <- unique(output)
  done <- merge(first, output, by.x=c("min_year", "max_year", var), by.y=c("year_min", "year_max", "name"))
  done$gender <- factor(done$gender, levels=c("male", "female"), labels=c("Male", "Female"))
  done <- done %>% select("pmid", "gender")
  colnames(done) <- c("pmid", paste0(var, "_gender"))
  done
}
