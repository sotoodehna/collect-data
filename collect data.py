#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyranges as pr
import pandas as pd
import glob 
import os
H = ["chr",  "start", "stop", "strand", "gene_symbol", "entrez_gene_id", "transcript_id" , "raw_count", "scaled_estimate", "normalized_count"]
list = os.listdir("E:\\data\\HG19_TCGA_rnaseqv2_isoform\\bedfiles")   # Path to the main directory
newList = []
for i in range(len(list)):
    newList.append("E:\\data\\HG19_TCGA_rnaseqv2_isoform\\bedfiles\\" + list[i])
for bed in newList:
    df = pr.read_bed(bed, as_df=True)
    filename = df.to_excel('E:\\data.xlsx',mode ='a', header = H, index=False)

