# Drug_Response_Prediction
Computational drug response prediction using transcriptomic data

Goal:
Run both continuous and binned response predictions.  
Computational, pathway informed, and random feature selection
Benchmark conventional grid ML vs. Keras API / Tensorflow

Questions:
Cancer-type specific? - get tissue of origin associated with cell line from BMEG?

2021-11-04

Reset with coding genes and 50% RFE cut.

v3 branch started. ---> end v2 iterations <---

2021-10-29.    

long_jobs directory and scripts set on exacloud.  

2021-10-19  
Next-actions:  
  Check-in drg_rsp_v2.ipynb.     
  Build and check-in CCLE drug-resp (querry).   
  Build and check-in code for CCLE gene expression by cell line.   
CCLE object from expression chunks. 
  exp_chnks nb:_________.  
  
  Build and check drug_response_CTRPv2.   
  drg_rsp ctrp nb:________.  
  
Need to do subsetting of files on exacloud

2021-10-18  
Reproduce generation of CTRPv2_16_beta_bromoandrosterone.tsv
  (in data directory)
  
Requires mapping of cell lines to drug response object
Timing of querries 
