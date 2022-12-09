def proteins(strand):
    cod_prot = {"Methionine": ("AUG"),
                "Phenylalanine": ("UUU", "UUC"),
                "Leucine": ("UUA", "UUG"),
                "Serine": ("UCU", "UCC", "UCA", "UCG"),
                "Tyrosine": ("UAU", "UAC"),
                "Cysteine": ("UGU", "UGC"),
                "Tryptophan": ("UGG"),
                }

    stop = ["UAA", "UAG", "UGA"]

    codons = []
    proteins = []
    c = 0
    for i in range(len(strand)):
        if c == len(strand):
            break
        else:
            codons.append(strand[c:c + 3])
            c += 3

    d = 0
    for i in range(len(codons)):
        if d == 0:
            for j, k in cod_prot.items():
                if codons[i] in k:
                    proteins.append(j)
                elif codons[i] in stop:
                    d += 1

    return proteins
    
