
import argparse
import copy
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from time import gmtime, strftime
from genomedisco import data_operations, processing, visualization

#from https://stackoverflow.com/questions/6076770/ignore-importerror-when-exec-source-code
#this allows us to import functions from hic-spector without having to install modules that get imported there such as straw
import __builtin__
from types import ModuleType

class DummyModule(ModuleType):
    def __getattr__(self, key):
        return None
    __all__ = []   # support wildcard imports

def tryimport(name, globals={}, locals={}, fromlist=[], level=-1):
    try:
        return realimport(name, globals, locals, fromlist, level)
    except ImportError:
        return DummyModule(name)

realimport, __builtin__.__import__ = __builtin__.__import__, tryimport
#=======================================
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))+"/HiC-spector/")
from run_reproducibility import get_Laplacian, evec_distance, get_ipr, get_reproducibility 
import StringIO

def main():
    parser = argparse.ArgumentParser(description='Wrapper for HiC-Spector')
    parser.add_argument('--m1')
    parser.add_argument('--m2')
    parser.add_argument('--node_file')
    parser.add_argument('--num_evec',type=int,default=20)
    parser.add_argument('--out')
    args = parser.parse_args()
    
    nodes,nodes_idx,blacklist_nodes=processing.read_nodes_from_bed(args.node_file,'NA')
    m1=processing.construct_csr_matrix_from_data_and_nodes(args.m1,nodes,blacklist_nodes,True)
    m2=processing.construct_csr_matrix_from_data_and_nodes(args.m2,nodes,blacklist_nodes,True)
    sys.stdout = open(args.out, 'w')
    get_reproducibility(m1,m2,args.num_evec)

main()
