#!/usr/bin/env R


# functions
rmdatexists <- function(){return()}

#----------------
# RemethDL class
#----------------
setClass("RemethDL", representation(baseurl = "character")
         # , contains = "superclass" # check for existing url connector classes
)
# methods
setMethod("check", function(){rmdatexists()})


#------------------------
# Managing file downloads
#------------------------

# getfiles list from server

# identify 


# `RemethDL` class contains metadata for download management of Recount Methylation data.



# Instantiate RemethDL instance and populate
rmdl <- list()
class(rmdl) <- "RemethDL"

# Get files based on data in 


# Utilities for accessing H5SE data

urltodat = "ftp://recount.bio/data/"


#' Get the latest fn
#'
#' Get a dataset connection object from an HDF5 database 
#' ('.h5') file and return the indexed table subset.
#' @param ri rows indices in dataset.
#' @param ci columns indices in dataset.
#' @param dsn Name of dataset or group of dataset to connect with.
#' @param dbn Path to h5 database file.
#' @return HDF5 database connection object.
#' @examples
#' fn = latest_h5se()
#' @export
latest_h5se <- function(url = urltodat){
  
  # get filenames list from urltodat
  # fnl <- getURL(url) 
  
  # sort on version and ts in fn
  
  # return latest h5se data dir names
  
  return(c(fn1, fn2, fn3))
}

get_h5se <- function(whichdat = c("all", "rg", "gr", "gm")){
  
  
  
  # sort by timestamp and version
  
  
  # 
  url <- "https://recount.bio/data"
  dir <- dfp <- "remethdb_h5se_gm_00-00-01_1583780004"
  url <- paste(url, dir, sep = "/")
  dlf <- download.file(url, dfp)
  
}


