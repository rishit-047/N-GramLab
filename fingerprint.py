import hashlib
import numpy as np

# -------------------------------------------------------------
# Function: stable_hash
# -------------------------------------------------------------
# Purpose:
#   Convert an n-gram into a stable integer hash.
#   This ensures that the same input always produces the same output hash
#   even across machines or runs.
#
# Steps:
#   1. Encode text into bytes (hash functions work on bytes).
#   2. Compute a BLAKE2b hash (digest_size=8 → 64-bit hash).
#   3. Convert the hexadecimal hash output into an integer.
#   4. Reduce it into a fixed range [0, bits) using modulo operation.
# -------------------------------------------------------------
def stable_hash(text, bits):
    # Converting text into bytes. Needed for hashing
    encoded = text.encode()

    # Computing a BLAKE2b hash (digest_size = 8 -> 64 bit hash)
    digest = hashlib.blake2b(encoded, digest_size=8).hexdigest()

    # Converting the hexadecimal digest to an integer
    h = int(digest, 16)

    # Reducing it into a fixed range -> [0 to bits] to map its to a bitvector index
    return h % bits

# -------------------------------------------------------------
# Function: build_bitvector
# -------------------------------------------------------------
# Purpose:
#   Convert a set of n-grams into a fixed-length bitvector fingerprint.
#
# How it works:
#   1. Initialize a bitvector of zeros (length = bits).
#   2. For each n-gram:
#       - Hash the n-gram string into a stable index.
#       - Set the bit at that index to 1.
# -------------------------------------------------------------
def build_bitvector(ngrams, bits):

    # Creating an all zero bitvector of size bits
    bitvector = np.zeros(bits, dtype=np.uint8)

    # for each n-gram, compute its hash & activates the bit at that index
    for ngram in ngrams:
        index = stable_hash(",".join(ngram), bits)
        bitvector[index] = 1

    # Returning the final fingerprint vector
    return bitvector

# -------------------------------------------------------------
# Function: build_topk
# -------------------------------------------------------------
# Purpose:
#   Extract the top-K most frequent n-grams from a Counter object.
# -------------------------------------------------------------
def build_topk(ngrams_counter, k):
    
    # get top k most common n-grams
    return ngrams_counter.most_common(k)
