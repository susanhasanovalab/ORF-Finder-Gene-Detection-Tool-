print("ORF Finder (Gene Detection Tool)\n")
dna = input("Enter DNA sequence: ").upper()
start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]
orfs = []

for i in range(len(dna) - 2):
    codon = dna[i:i+3]
    
    if codon == start_codon:
        for j in range(i+3, len(dna)-2, 3):
            stop_codon = dna[j:j+3]
            
            if stop_codon in stop_codons:
                orf = dna[i:j+3]
                orfs.append((i, j+3, orf))
                break

print("\n Found ORFs:\n")

if orfs:
    for idx, (start, end, seq) in enumerate(orfs):
        print(f"ORF {idx+1}:")
        print(f"Start: {start}, End: {end}")
        print(f"Sequence: {seq}\n")
else:
    print("No ORFs found.")

print("📊 This is a simplified gene prediction model.")