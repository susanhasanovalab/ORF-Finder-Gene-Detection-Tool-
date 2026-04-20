import numpy as np
from sklearn.ensemble import RandomForestClassifier

start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]

def find_orfs(dna):
    orfs = []
    for i in range(len(dna) - 2):
        if dna[i:i+3] == start_codon:
            for j in range(i+3, len(dna)-2, 3):
                if dna[j:j+3] in stop_codons:
                    orf_seq = dna[i:j+3]
                    orfs.append(orf_seq)
                    break
    return orfs

def extract_features(orf):
    length = len(orf)
    gc_content = (orf.count("G") + orf.count("C")) / length
    at_content = (orf.count("A") + orf.count("T")) / length
    stop_density = sum(orf[i:i+3] in stop_codons for i in range(0, length-2, 3)) / (length/3)
    return [length, gc_content, at_content, stop_density]

training_data = [
    "ATGAAATTTGGGCCCTAA",
    "ATGCGTACGTAG",
    "ATGTTTAA",
    "ATGCCCCGGGTTTGA"
]

X = []
y = []

for seq in training_data:
    orfs = find_orfs(seq)
    for orf in orfs:
        X.append(extract_features(orf))
        y.append(1 if len(orf) > 15 else 0)

X = np.array(X)
y = np.array(y)

model = RandomForestClassifier()
model.fit(X, y)

def predict_orf_quality(dna):
    orfs = find_orfs(dna)
    results = []
    for orf in orfs:
        features = np.array(extract_features(orf)).reshape(1, -1)
        score = model.predict_proba(features)[0][1]
        results.append((orf, score))
    return results

dna_input = input().upper()
results = predict_orf_quality(dna_input)

for orf, score in results:
    print(orf, score)
