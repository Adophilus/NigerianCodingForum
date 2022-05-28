proteinsMapping = {
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

stop_codon = "---"

def processProteinChain(proteinChain):
    chain_length = len(proteinChain)
    proteins = []
    i = 0
    for j in range(3, chain_length, 3):
        protein = proteinsMapping[proteinChain[i:j]]
        if (protein == stop_codon):
            break
        proteins.append(protein)
        i = j
    return [ tuple(proteins), len(set(proteins)) ]

print(processProteinChain(input()))
