def gc(dna) :
    "this function computes the GC percentage of a dna sequence"
    nbases=dna.count('n') + dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C') +dna.count('g')