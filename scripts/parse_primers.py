#! /usr/bin/env python   
""" Basic parser for the Rhim Thunderbolts manifest file. """

import sys, os, re
import pybedtools
#import pandas as pd
#import cPickle as pickle




class PrimerPairRecord(object):
    """Represents a primer pair derived from a MiSeq manifest. """

    def __init__(self, id, target_id, primer_set, chrom, original_start, original_end, converted_end, converted_start, genome_build, sense_start,
                 antisense_start, sense_sequence, antisense_sequence, sense_sequence_tailed_illumina, antisense_sequence_tailed_illumina):
        self.id = id
        self.target_id = target_id
        self.primer_set = primer_set
        self.chrom = chrom
        self.orginal_start = int(original_start)
        self.original_end = int(original_end)
        self.converted_start = int(converted_start)
        self.converted_end = int(converted_end)
        self.genome_build = genome_build
        self.sense_start = int(sense_start)
        self.antisense_start = int(antisense_start)
        self.sense_sequence = sense_sequence
        self.antisense_sequence = antisense_sequence
        self.sense_sequence_tailed_illumina = sense_sequence_tailed_illumina
        self.antisense_sequence_tailed_illumina = antisense_sequence_tailed_illumina

    
    @property
    def to_fasta(self):
        fa_header1 = ">{0}_{1}_{2}_F".format(self.id, self.target_id, self.sense_sequence)
        outline1 = "{0}\n{1}\n".format(fa_header1, self.sense_sequence.upper())
        fa_header2 = ">{0}_{1}_{2}_R".format(self.id, self.target_id, self.sense_sequence)
        outline1 = "{0}\n{1}\n".format(fa_header1, self.sense_sequence.upper())





def parse_thunderbolts_manifest(filename):
    """ Parses a Rhim manifest file to pull out primer data. Returns a dict. """
    primer_l = []
    datafile = file(filename)
    header = datafile.readline()
    for line in datafile.readlines():
        bits = line.strip().split("\t")
        pr = PrimerPairRecord(*bits[0:15])
        primer_l.append(pr)
    return primer_l






if __name__ == '__main__':

   if (len(sys.argv) != 2):
        print "usage: {0} [thunderbolts manifest]".format(os.path.basename(sys.argv[0]))
        sys.exit() 

   primers = parse_thunderbolts_manifest(sys.argv[1])
   print primers[0]


   print "done."