import numpy as np

# -------------------------------------------------------------
# Function: jaccard_bitvector
# -------------------------------------------------------------
# Purpose: Compute the Jaccard similarity between two bitvectors.
# Formula: J(A, B) = |A ∩ B| / |A ∪ B|
# Interpretation:
#   - 1.0 means the two fingerprints are identical
#   - 0.0 means they have no overlap at all
#
# Example:
#   A = [1,0,1,0,1]
#   B = [1,1,0,0,1]
#   Intersection = 2  (positions with 1 in both)
#   Union = 4         (positions with 1 in either)
#   → Jaccard = 2 / 4 = 0.5
# -------------------------------------------------------------
def jaccard_bitvector(a, b):
    intersection = np.bitwise_and(a, b).sum()
    union = np.bitwise_or(a, b).sum()
    if union == 0:
        return 0.0

    return intersection / union

# -------------------------------------------------------------
# Function: hamming_similarity
# -------------------------------------------------------------
# Purpose: Compute similarity based on Hamming distance.
# Formula: Hamming similarity = 1 - (number of differing bits / total bits)
# Interpretation:
#   - 1.0 → identical fingerprints
#   - 0.0 → completely different
#
# Example:
#   A = [1,0,1,0]
#   B = [1,1,0,0]
#   XOR = [0,1,1,0] → diff = 2
#   → Similarity = 1 - 2/4 = 0.5
# -------------------------------------------------------------
def hamming_similarity(a, b):
    diff = np.bitwise_xor(a, b).sum()
    return 1 - diff / len(a)