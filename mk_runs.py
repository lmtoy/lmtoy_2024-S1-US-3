#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-03"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['Taurus_Peak'] = [ 125399, 125409, 125421, 125576, 125578 ]
on['Taurus_Edge'] = [ 125403, 125405, 125407 ]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['Taurus_Peak']   = ""
pars1['Taurus_Edge']   = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2['Taurus_Peak']   = "srdp=1 admit=0"
pars2['Taurus_Edge']   = "srdp=1 admit=0"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3['Taurus_Peak']   = "srdp=1 admit=0"
pars3['Taurus_Edge']   = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
