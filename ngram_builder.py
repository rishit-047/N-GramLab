from collections import Counter

def build_ngrams(tokens, n):
    
    """"
    Build n-grams from a sequence of syscall tokens and count their frequencies.

    Args:
        tokens (list): List of syscall names (e.g., ["open", "read", "write", "close"]).
        n (int): Size of each n-gram (e.g., 3 for 3-grams).

    Returns:
        Counter: A dictionary-like object mapping each n-gram tuple to its frequency count.

    """

    # Storing all n-grams 
    ngrams = []

    # Slide a window of size 'n' across the list of syscalls
    # Eg - tokens [a,b,c,d], n = 3 -> (a,b,c), (b,c,d)
    for i in range(len(tokens)-n+1):
        
        # Extracting n consecutive tokens starting at position i
        ngram = tuple(tokens[i:i+n])
        ngrams.append(ngram)

    #Counting how many times each n-gram appears
    ngram_count = Counter(ngrams)

    # Returning frequency map
    return ngram_count

