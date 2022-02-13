#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) University of St Andrews 2020-2021
# (c) University of Strathclyde 2020-2021
# (c) James Hutton Institute 2020-2021
#
# Author:
# Emma E. M. Hobbs
#
# Contact
# eemh1@st-andrews.ac.uk
#
# Emma E. M. Hobbs,
# Biomolecular Sciences Building,
# University of St Andrews,
# North Haugh Campus,
# St Andrews,
# KY16 9ST
# Scotland,
# UK
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Functions for compiling and writing out test sets"""

from Bio.Blast.Applications import NcbiblastpCommandline

QUERY_FASTA = "data/cluster_data/remaining_fam_seqs.fasta"
SUBJECT_FASTA = "data/cluster_data/all_clusters.fasta"
OUTPUT = "supplementary/cluster_data/remaining_fam_seqs_blastp.tsv"

all_v_all_blastp = NcbiblastpCommandline(
    query=QUERY_FASTA,
    subject=SUBJECT_FASTA,
    out=OUTPUT,
    outfmt="6 qseqid sseqid pident qcovs qlen slen length bitscore evalue",
)
stdout, stderr = all_v_all_blastp()

# check if alignment was successful
if len(stderr) != 0:
    print(stderr)

print("Written alignemnt output to:\n", OUTPUT)