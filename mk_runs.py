#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-3"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['Taurus_Edge'] = [ 125403, 125405, 125407,
                      125699, 125701, 125703, 125705, 125707,]
on['Taurus_Peak'] = [ 125399, 125409, 125421,-125576, 125578,
                      125687, 125689,]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['Taurus_Peak']   = "pix_list=0,1,2,3 dv=4 dw=8 vlsr=6 b_order=1"
pars1['Taurus_Edge']   = "pix_list=0,1,2,3 dv=4 dw=8 vlsr=6 b_order=1"
# birdies only in pixel=2 but more complex than usual?

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2['Taurus_Peak']   = "pix_list=0,2 bank=0"
pars2['Taurus_Edge']   = "pix_list=0,2 bank=0"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3['Taurus_Peak']   = "pix_list=1,3 bank=1"
pars3['Taurus_Edge']   = "pix_list=1,3 bank=1"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
