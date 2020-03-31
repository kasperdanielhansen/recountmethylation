# does validation of se H5SE objects vs. GEO

# obtain download info


#-----------------
# HIDDEN FUNCTIONS
#-----------------

# validate
validate_gsms <- function(gsmids){
  # gsmids : sample gSM IDS whose methylation data to validate
  
  
  dn = "" # download idats to cwd
  bnv = c() # store the idat basenames
  for(gsmi in gsmvi){
    url = paste0("ftp://ftp.ncbi.nlm.nih.gov/geo/samples/", 
                 substr(gsmi, 1, nchar(gsmi)-3), 
                 paste(rep("n", 3), collapse = ""), 
                 "/", gsmi, "/suppl/")
    # get urls to idats
    if(require(RCurl)){
      fn = RCurl::getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE) 
    }
    fn <- unlist(strsplit(fn, "\n"))
    fn = unlist(fn)[grepl("\\.idat\\.gz", fn)] # retain valid idat paths
    bnv = c(bnv, unique(gsub("_Red.*|_Grn.*", "", fn))) # retain idat basenames
    for(f in fn){
      dfp = paste(getwd(), "/", dn, "/", f, sep = "")
      download.file(paste(url, f, sep = ""), dfp)
      system(paste0("gunzip ", dfp))
      message(f)
    }
    message(gsmi)
  }
  
}

#
# options, likely not necessary
# analysis ()