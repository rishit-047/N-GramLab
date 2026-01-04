# NgramLab – Syscall Behavioral Fingerprinting Tool

NgramLab is a Python-based cybersecurity tool that performs **behavioral fingerprinting of programs using system call (syscall) n-grams**.  
Instead of relying on static signatures, NgramLab analyzes **runtime behavior** captured via `strace` and generates compact fingerprints that can be compared to identify **malware, variants, or similar binaries**.

---

## Cybersecurity Use Cases

- Malware detection using runtime syscall behavior
- Behavioral similarity analysis between binaries
- Detection of malware variants and polymorphic samples
- Dynamic analysis of unknown executables
- Research and academic projects in system security

---

## How It Works


1. Capture system calls using `strace`
2. Normalize and tokenize syscalls
3. Construct syscall n-grams
4. Hash n-grams into a fixed-size bitvector
5. Extract top-k frequent n-grams
6. Compare fingerprints using similarity metrics

---

## Requirements

- Linux (Ubuntu / Kali / Debian-based)
- Python 3.7 or higher
- `strace` utility

---

## Installation

1) Clone the repository using the following link:
   ```bash
   git clone https://github.com/rishit-047/N-GramLab.git

2) Navigate inside the N-GramLab directory and run the following command:
   ``` bash
   chmod +x ngramlab
   
### Flag Explanations

- **`-h, --help`**  
  Displays the help menu showing all available options and exits the program.

- **`-i, --input INPUT`**  
  Specifies the input syscall trace file generated using `strace`.  
  This file contains raw system call logs of the executed program.  
  Supported formats include `.log`, `.trace`, and `.txt`.

- **`-o, --output OUTPUT`**  
  Specifies the output file where the generated fingerprint results will be saved.  
  The output includes top-k n-grams and a summary of the bitvector fingerprint.

- **`-k K`**  
  Defines how many of the most frequent syscall n-grams should be displayed.  
  If not provided, the default value is **5**.

- **`-n N`**  
  Sets the size of the n-grams to be generated from syscall sequences.  
  For example, `n=3` generates syscall 3-grams.  
  The default value is **3**, which is commonly used in behavioral analysis.

- **`-t`**  
  If this flag is specified, the results are displayed in the terminal in addition to being written to the output file.  
  If not specified, the program runs silently and only writes to the output file.

- **`-bv BV`**  
  Specifies the size (length) of the bitvector fingerprint.  
  Larger values reduce hash collisions but require more memory.  
  The default size is **1024 bits**.

- **`--compare FILE1, FILE2`**  
  Enables comparison mode.  
  When this option is used, NgramLab generates fingerprints for **two syscall trace files** and compares them using similarity metrics such as **Jaccard similarity** and **Hamming similarity**.  
  This mode is useful for determining whether two programs exhibit similar runtime behavior (e.g., malware variant detection).

---

