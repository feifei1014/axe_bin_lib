#!/usr/bin/python3

import argparse

#from axesrc import axetasks
from axesrc.log_utils import set_logging
from axesrc.extract1d import Extract1D
#_log = set_logging(filename='axe_output.log')
#_log.info('start!')

def parse_args():
    """Parses command line arguments.

    Parameters:
        nothing

    Returns:
        args : argparse.Namespace object
            An argparse object containing all of the added arguments.

    Outputs:
        nothing
    """

    #Create help string:
    gpath_help = 'Path to grating file.'
    # Add arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpath', '-gpath', dest = 'gpath', action = 'store',
                        type = str, required = True, help = gpath_help)

    #Create help string:
    cpath_help = 'Path to object catalogue.'
    # Add arguments:
    parser.add_argument('--cpath', '-cpath', dest = 'cpath', action = 'store',
                        type = str, required = True, help = cpath_help)

    #Create help string:
    bpath_help = 'Path to the Master Sky image.'
    # Add arguments:
    parser.add_argument('--bpath', '-bpath', dest = 'bpath', action = 'store',
                        type = str, required = True, help = bpath_help)

    #Create help string:
    opath_help = 'Path to pull SPC/STP file.'
    # Add arguments:
    parser.add_argument('--opath', '-opath', dest = 'opath', action = 'store',
                        type = str, help = opath_help)

    #Create help string:
    inpath_help = 'Path to axe input files.'
    # Add arguments:
    parser.add_argument('--inpath', '-inpath', dest = 'inpath', action = 'store',
                        type = str, help = inpath_help)
    
    #Create help string:
    outpath_help = 'Path to axe output files.'
    # Add arguments:
    parser.add_argument('--outpath', '-outpath', dest = 'outpath', action = 'store',
                        type = str,help = outpath_help)

    #Create help string:
    confpath_help = 'Path to axe configs.'
    # Add arguments:
    parser.add_argument('--confpath', '-confpath', dest = 'confpath', action = 'store',
                        type = str, help = confpath_help)

    binpath_help = 'Path to axe bins.'
    # Add arguments:
    parser.add_argument('--binpath', '-binpath', dest = 'binpath', action = 'store',
                        type = str, required = True, help = binpath_help)

    # Parse args:
    args = parser.parse_args()

    return args
if __name__ == '__main__':

    args = parse_args()

    grating = args.gpath
    objcat = args.cpath
    bckimg = args.bpath
    binpath = args.binpath
    if args.opath:
        spcpath = args.opath
    else:
        spcpath = '/app/data'

    if args.inpath:
        inputpath = args.inpath 
    else:
        inputpath = None
    if args.outpath:
        outputpath = args.outpath 
    else:
        outputpath = None
    if args.confpath:
        confpath = args.confpath
    else:
        confpath = None

    tst = Extract1D(gratingfile=grating,
                    objcat=objcat,
                    inputpath=inputpath, confpath=confpath, outputpath=outputpath,binpath=binpath,
                    indir_overlap=True,
                    outdir_overlap=True,
                    bckimg=bckimg,
                    spcpath = spcpath)
