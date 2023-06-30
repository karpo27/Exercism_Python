def to_rna(dna_strand):

    rna_strand = []
    for i in list(dna_strand):
        if i == "G":
            rna_strand.append("C")
        elif i == "C":
            rna_strand.append("G")
        elif i == "T":
            rna_strand.append("A")
        elif i == "A":
            rna_strand.append("U")

    return "".join(rna_strand)
    
