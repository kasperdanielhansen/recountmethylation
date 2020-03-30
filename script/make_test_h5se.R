#!/usr/bin/env R

library(DelayedArray)

# 

# 

path.to.h5se <- paste0(".", "recount.bio", "data", 
                       collapse = "/")

lfh5se <- list.files(path.to.h5se)