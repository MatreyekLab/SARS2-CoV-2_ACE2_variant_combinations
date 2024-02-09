#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sys
import pandas as pd

print("enter file path with 2A sequences.  Reference 2A should be the first entry.")
# should be csv file.  Row one is expected to be a header.
# Sequences should be aligned..  Sequences are expected to be the same length.
# At the present time, a * paired with any other amino acid adds 100,000 to the score in order to greatly differentiate sequences with a stop codon.
# Solo grantham scores, such as A versus '-', were calculated using 0 for c_j, p_j, and v_j
Grantham = pd.DataFrame(pd.read_csv("Grantham.csv"))
Grantham_Decode = pd.DataFrame(pd.read_csv("Grantham_Decode.csv"))
textfile = pd.DataFrame(pd.read_csv(input("Path: " )))

# line 14 through 35 confirm that the file will work correctly.
textfile_length = len(textfile) - 1

lengths = []
i = 0
while i < textfile_length:
    entry = textfile.iat[i,1]
    entry_length = len(entry)
    lengths.append(entry_length)
    i = i+1

i = 1
initial = lengths[0]
while i < (len(lengths)-1):
    compare = lengths[i]
    if initial != compare:
        print("There is a length mismatch: " + i)
        exit()
    i = i+1

Reference = textfile.iat[0,1]
Seq_Length = len(Reference)-1

# line 38 through 62 generates an updated file with columns containing total grantham score, and grantham score by position.  All is relative to the first entry of the input file.
i = 0
Scores = []
Score_List = []
while i <= textfile_length:
    Other = textfile.iat[i,1]
    j = 0
    Score = 0
    Score_Per_Residue = []
    while j<= Seq_Length:
        Next_Residue_Reference = Reference[j]
        Next_Residue_Other = Other[j]
        Next_Residue_Numeric_Reference = Grantham_Decode.index[Grantham_Decode["Residue"] == Next_Residue_Reference].tolist()
        Next_Residue_Numeric_Other = Grantham_Decode.index[Grantham_Decode["Residue"] == Next_Residue_Other].tolist()
        Score = Score + Grantham.iat[Next_Residue_Numeric_Reference[0],Next_Residue_Numeric_Other[0]]
        Score_Per_Residue.append(Grantham.iat[Next_Residue_Numeric_Reference[0],Next_Residue_Numeric_Other[0]])
        j = j+1
    Scores.append(Score)
    Score_List.append(Score_Per_Residue)
    i = i+1
    
textfile['Sequence_Grantham_Distance'] = Scores
textfile['Sequence_Grantham_Distance_Per_Residue'] = Score_List

textfile.to_csv("Updated_Sequence_file.csv", sep = ',', encoding = 'utf-8')
print("New file saved as Updated_Sequence_file.csv")

# line 65 through 90 generates a file with a matrix of grantham scores.  Matrix order matches order of input file.
k = 0
Mega_List = []
while k <= textfile_length:
    Reference = textfile.iat[k,1]
    i = 0
    Scores = []
    while i <= textfile_length:
        Other = textfile.iat[i,1]
        j = 0
        Score = 0
        while j<= Seq_Length:
            Next_Residue_Reference = Reference[j]
            Next_Residue_Other = Other[j]
            Next_Residue_Numeric_Reference = Grantham_Decode.index[Grantham_Decode["Residue"] == Next_Residue_Reference].tolist()
            Next_Residue_Numeric_Other = Grantham_Decode.index[Grantham_Decode["Residue"] == Next_Residue_Other].tolist()
            Score = Score + Grantham.iat[Next_Residue_Numeric_Reference[0],Next_Residue_Numeric_Other[0]]
            j = j+1
        Scores.append(Score)
        i = i+1
    Mega_List.append(Scores)
    k = k+1

Grantham_Matrix = pd.DataFrame(Mega_List)

Grantham_Matrix.to_csv("Sequence_matrix.csv", sep = ',', encoding = 'utf-8')
print("New file saved as Sequence_matrix.csv, columns match rows of original file")

