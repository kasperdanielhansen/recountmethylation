#!/usr/bin/env python 3

""" ftpcall
gets latest files for RM data
"""

fn1 = "remethdb_h5se_gm_00-00-01_1583780004"
fn2 = "remethdb_h5se_gr_00-00-01_1583780004"
fn3 = "remethdb_h5se_rg_00-00-01_1583780004"

ftp = "ftpstring"
ftp.call = ftp + fn1

def getlatest_filepath(filepath, filestr, embeddedpattern=False, tslocindex=1,
    returntype='returnstr'):
    """ getlatest_filepath
        Get path the latest version of a file, based on its timestamp. Can 
        return >1 files sharing latest timestamp as type list or str.
        Arguments:
            * filepath (str) : Path to directory to search.
            * filestr (str) : Pattern of filename filter for search.
            * embeddedpattern (T/F, bool) : Whether filestr pattern is embedded
                in filename (assumes pattern at start of name otherwise)
            * tslocindex (int) : Relative location index of timestamp in fn.
            * returntype (str) : Return file path(s) as str (use 'returnstr') or 
                list (use 'returnlist')
        Returns:
            * latest_file_path (str) or status (0, int) : Path to latest version 
                of file, or else 0 if search turned up no files at location
    """
import os

fn1 = "remethdb_h5se_gm_00-00-01_1583780004"
fn2 = "remethdb_h5se_gr_00-00-01_1583780004"
fn3 = "remethdb_h5se_rg_00-00-01_1583780004"
ftppath = "https://recount.bio/data"
ftp.call = str(os.path.join(ftppath, fn1))








ftp.path = str(os.path.join(ftppath, ftp.path))


    # print("start getlatest")
    if embeddedpattern:
        embedpattern = str('*' + filestr + '*')
        pathstr = str(os.path.join(filepath, embedpattern))
        filelist = glob.glob(pathstr)
    else:
        pathpattern = '.'.join([os.path.join(filepath, filestr), '*'])
        filelist = glob.glob(pathpattern)
    if filelist:
        flfilt = []
        # filter filelist on possible int/valid timestamp
        for fp in filelist:
            try:
                int(os.path.basename(fp).split('.')[tslocindex])
                flfilt.append(fp)
            except ValueError:
                break
        if flfilt and not len(flfilt)==0: 
            if len(flfilt) > 1:
                lfr = []
                # sort on timestamp
                flfilt.sort(key=lambda x: int(os.path.basename(x).split('.')[tslocindex]))
                # last list item
                lastitem = flfilt[-1]
                latestts = lastitem.split('.')[tslocindex]
                lfr = [flitem for flitem in flfilt
                    if flitem.split('.')[tslocindex] == latestts
                ]
            else:
                lfr = [flfilt[0]]
            # print("getlatest end")
            if returntype=='returnstr':
                return ' '.join(i for i in lfr)
            if returntype=='returnlist':
                return lfr
            else:
                return None
        else:
            return None
    else:
        return None 











def getlatest_filepath(filepath, filestr, embeddedpattern=False, tslocindex=1,
    returntype='returnstr'):
    """ getlatest_filepath
        Get path the latest version of a file, based on its timestamp. Can 
        return >1 files sharing latest timestamp as type list or str.
        Arguments:
            * filepath (str) : Path to directory to search.
            * filestr (str) : Pattern of filename filter for search.
            * embeddedpattern (T/F, bool) : Whether filestr pattern is embedded
                in filename (assumes pattern at start of name otherwise)
            * tslocindex (int) : Relative location index of timestamp in fn.
            * returntype (str) : Return file path(s) as str (use 'returnstr') or 
                list (use 'returnlist')
        Returns:
            * latest_file_path (str) or status (0, int) : Path to latest version 
                of file, or else 0 if search turned up no files at location
    """
    # print("start getlatest")
    if embeddedpattern:
        embedpattern = str('*' + filestr + '*')
        pathstr = str(os.path.join(filepath, embedpattern))
        filelist = glob.glob(pathstr)
    else:
        pathpattern = '.'.join([os.path.join(filepath, filestr), '*'])
        filelist = glob.glob(pathpattern)
    if filelist:
        flfilt = []
        # filter filelist on possible int/valid timestamp
        for fp in filelist:
            try:
                int(os.path.basename(fp).split('.')[tslocindex])
                flfilt.append(fp)
            except ValueError:
                break
        if flfilt and not len(flfilt)==0: 
            if len(flfilt) > 1:
                lfr = []
                # sort on timestamp
                flfilt.sort(key=lambda x: int(os.path.basename(x).split('.')[tslocindex]))
                # last list item
                lastitem = flfilt[-1]
                latestts = lastitem.split('.')[tslocindex]
                lfr = [flitem for flitem in flfilt
                    if flitem.split('.')[tslocindex] == latestts
                ]
            else:
                lfr = [flfilt[0]]
            # print("getlatest end")
            if returntype=='returnstr':
                return ' '.join(i for i in lfr)
            if returntype=='returnlist':
                return lfr
            else:
                return None
        else:
            return None
    else:
        return None 