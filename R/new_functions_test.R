#!/usr/bin/env R

# Utilities for accessing H5SE data

urltodat = "ftp://recount.bio/data/"

latest_h5se <- function(url = urltodat){
  
  # get filenames list from urltodat
  # fnl <- getURL(url) 
  
  # sort on version and ts in fn
  
  # return latest h5se data dir names
  
  return(c(fn1, fn2, fn3))
}

get_h5se <- function(){
  
  
  
  # sort by timestamp and version
  
  
  # 
  url <- "https://recount.bio/data"
  dir <- dfp <- "remethdb_h5se_gm_00-00-01_1583780004"
  url <- paste(url, dir, sep = "/")
  dlf <- download.file(url, dfp)
  
}


