def Residue_Substitutions():
   prospensities = {
      'A':[0.48, 0.35, 0.17], 'C':[0.32, 0.54, 0.14], 'D':[0.81, 0.09, 0.10], 
      'E':[0.93, 0.04, 0.03], 'F':[0.42, 0.42, 0.16], 'G':[0.51, 0.36, 0.13], 
      'H':[0.66, 0.19, 0.15], 'I':[0.39, 0.47, 0.14], 'K':[0.93, 0.02, 0.05], 
      'L':[0.41, 0.49, 0.10], 'M':[0.44, 0.20, 0.36], 'P':[0.78, 0.13, 0.09],
      'Q':[0.81, 0.10, 0.09], 'R':[0.84, 0.05, 0.11], 'S':[0.70, 0.20, 0.10], 
      'T':[0.71, 0.16, 0.13], 'V':[0.40, 0.50, 0.10], 'W':[0.49, 0.44, 0.07], 
      'Y':[0.67, 0.20, 0.13], 'N':[0.82, 0, 0.08]
      }
   seq_in = open('5.4_Secondary_structure.fasta')
   seq = ''
   for line in seq_in:
      if line[0] != '>':
         seq += line.strip()
   seq_out = ''
   for amino_acid in seq:
      A30 = prospensities[amino_acid][0]
      if A30 > 0.60:
         seq_out += amino_acid.upper()
      else:
         seq_out += amino_acid.lower()
   print(seq + '\n')
   print(seq_out)

def Secondary_structure_predict():
   prospensities = {
      'A':[1.45, 0.97], 'C':[0.77, 1.30], 'D':[0.98, 0.80], 'E':[1.53, 0.26], 
      'F':[1.12, 1.28], 'G':[0.53, 0.81], 'H':[1.24, 0.71], 'I':[1.00, 1.60], 
      'K':[1.07, 0.74], 'L':[1.34, 1.22], 'M':[1.20, 1.67], 'P':[0.59, 0.62],
      'Q':[1.17, 1.23], 'R':[0.79, 0.90], 'S':[0.79, 0.72], 'T':[0.82, 1.20],
      'V':[1.14, 1.65], 'W':[1.14, 1.19], 'Y':[0.61,1.29], 'N':[0, 0]
      }
   seq = ''
   seq_transformed = ''
   for line in open('5.4_Secondary_structure.fasta'):
      if line[0] != '>':
         seq +=line.strip().upper()
   print(seq + '\n')
   for amino_acid in seq:
      pref_H = prospensities[amino_acid][0]
      pref_E = prospensities[amino_acid][1]
      if pref_H >=1 and pref_E < pref_H:
         seq_transformed += 'H'
      elif pref_E >=1 and pref_H < pref_E:
         seq_transformed += 'E'
      else:
         seq_transformed += 'L'
   print(seq_transformed)

def protein_disorder_predictor():
   propensities = {
   'N': 0.2299, 'P': 0.5523, 'Q':-0.18770, 'A':-0.2615,
   'R':-0.1766, 'S': 0.1429, 'C':-0.01515, 'T': 0.0089,
   'D': 0.2276, 'E':-0.2047, 'V':-0.38620, 'F':-0.2256,
   'W':-0.2434, 'G': 0.4332, 'H':-0.00120, 'Y':-0.2075,
   'I':-0.4222, 'K':-0.1001, 'L': 0.33793, 'M':-0.2259
   }

   threshold = 0.3

   input_seq = "IVGGYTCGANTVPYQVSLNSGYHFCGGSLINSQWVVSAAHCYKSG\
   IQVRLGEDNINVVEGNEQFISASKSIVHPSYNSNTLNNDIMLIKLKSAASLNSR\
   VASISLPTSCASAGTQCLISGWGNTKSSGTSYPDVLKCLKAPILSDSSCKSAYP\
   GQITSNMFCAGYLEGGKDSCQGDSGGPVVCSGKLQGIVSWGSGCAQKNKPGVYT\
   KVCNYVSWIKQTIASN"

   output_seq = ""

   # Cycle over every amino acid in inputSeq
   for res in input_seq: 
      if res in propensities:
         if propensities[res] >= threshold:
            output_seq += res.upper()
         else:
            output_seq += res.lower()
      else:
         print('unrecognized character:', res)
         break

   print(output_seq)

#Residue_Substitutions()
protein_disorder_predictor()
#Secondary_structure_predict()
function = input('>:')
print(function)
if function == '1':
   Residue_Substitutions()
elif function == '2':
   protein_disorder_predictor()
else:
   Secondary_structure_predict()
