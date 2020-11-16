#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyranges as pr
import pandas as pd
import os

H = ["chr",  "start", "stop", "strand", "gene_symbol", "entrez_gene_id", "transcript_id" , "raw_count", "scaled_estimate", "normalized_count", "barcode"]
list = os.listdir("E:\\data\\HG19_TCGA_rnaseqv2_isoform\\bedfiles")
num = len(list)
x = 0 
name =[]
newList = []

for f in list:
    x = '-'.join(f.split('-')[0:3])
    name.append(x)
    
for i in range(len(list)):
    newList.append("E:\\data\\HG19_TCGA_rnaseqv2_isoform\\bedfiles\\" + list[i])
    
for bed in newList:
    for n in name:
        df = pr.read_bed(bed, as_df=True)
        df['barcode'] = n
        filename = df.to_csv('E:\\data11.csv',mode ='a', header = H, index=False)

