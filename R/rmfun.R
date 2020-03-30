#!/usr/bin/env R

# https://stackoverflow.com/questions/16699856/get-website-directory-listing-in-an-r-vector-using-rcurl/17187525

# download files
url <- "https://recount.bio/data/"
rd <- RCurl::getURL(url)
gsub('.*\"', "", gsub('.*\"', "", rd))

RCurl::getURLContent(url, 
                     ftp.use.epsv = F)
RCurl::getURL(url)