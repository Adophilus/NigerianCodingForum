# Challenge

In order for protein to be formed, a chain of amino acids must be formed. These amino acids are formed with 3 base pairs. An example would be 'CUU' makes a Leucine ('Leu') amino acid. Remember that there are stop codons UAG, UGA, UAA which essentially ends the protein synthesis formation. This leaves you with a chain of amino acids that will be folded into a protien which hopefully becomes part of your python brain tissue!

The function to be built, amino_acids, must return a list of a tuple and an integer when given a string of mRNA code. The first tuple must contain all the amino acids and the integer must be the number of distinct amino acids. You can use the dictionary below to help with your function. The function must also not include the stop codon codes.

**NOTE:**
For this piece of code, we'll assume that there's only one stop codon in the sequence

```json
{
  "CUU": "Leu",
  "UAG": "---",
  "ACA": "Thr",
  "AAA": "Lys",
  "AUC": "Ile",
  "AAC": "Asn",
  "AUA": "Ile",
  "AGG": "Arg",
  "CCU": "Pro",
  "ACU": "Thr",
  "AGC": "Ser",
  "AAG": "Lys",
  "AGA": "Arg",
  "CAU": "His",
  "AAU": "Asn",
  "AUU": "Ile",
  "CUG": "Leu",
  "CUA": "Leu",
  "CUC": "Leu",
  "CAC": "His",
  "UGG": "Trp",
  "CAA": "Gln",
  "AGU": "Ser",
  "CCA": "Pro",
  "CCG": "Pro",
  "CCC": "Pro",
  "UAU": "Tyr",
  "GGU": "Gly",
  "UGU": "Cys",
  "CGA": "Arg",
  "CAG": "Gln",
  "UCU": "Ser",
  "GAU": "Asp",
  "CGG": "Arg",
  "UUU": "Phe",
  "UGC": "Cys",
  "GGG": "Gly",
  "UGA": "---",
  "GGA": "Gly",
  "UAA": "---",
  "ACG": "Thr",
  "UAC": "Tyr",
  "UUC": "Phe",
  "UCG": "Ser",
  "UUA": "Leu",
  "UUG": "Leu",
  "UCC": "Ser",
  "ACC": "Thr",
  "UCA": "Ser",
  "GCA": "Ala",
  "GUA": "Val",
  "GCC": "Ala",
  "GUC": "Val",
  "GGC": "Gly",
  "GCG": "Ala",
  "GUG": "Val",
  "GAG": "Glu",
  "GUU": "Val",
  "GCU": "Ala",
  "GAC": "Asp",
  "CGU": "Arg",
  "GAA": "Glu",
  "AUG": "Met",
  "CGC": "Arg"
}
```

`---` represents the stop codons

### Example

|Input|Output|
|-----|------|
|AUGUCGGCACAUUUAUGCUCCUAAUCC|[('Met', 'Ser', 'Ala', 'His', 'Leu', 'Cys', 'Ser'), 6]|


### Summary

- The output must be a list of a tuple of strings (amino acid) and a single integer (number of distinct amino acids)
- Must use the dictionary to call the amino acid or stop codon
- Must convert the three codes into an amino acid and stop at the stop codon (the function assumes all the codes have only one stop codon)
