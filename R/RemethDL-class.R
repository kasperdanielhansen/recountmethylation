#!/usr/bin/env R

# Functions and classes for managing Recount Methylation data downloads

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
