#!/usr/bin/env R

# download files
url <- "https://recount.bio/data/"
RCurl::getURL(url, ftp.use)

RCurl::getURLContent(url)
RCurl::getURL(url)