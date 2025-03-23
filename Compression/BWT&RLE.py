# Function to perform the Burrows-Wheeler Transform (BWT)
def bwt_transform(sequence):
    # Append a special character ($) to mark the end of the string
    sequence += "$"
    
    # Generate all cyclic rotations of the string
    cyclic_rotations = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
    
    # Sort the rotations lexicographically
    cyclic_rotations_sorted = sorted(cyclic_rotations)
    
    # The BWT is the last column of the sorted rotations
    bwt_result = ''.join(rotation[-1] for rotation in cyclic_rotations_sorted)
    
    return bwt_result

# Function to perform Run-Length Encoding (RLE)
def run_length_encoding(bwt_result):
    rle_result = []
    count = 1
    
    for i in range(1, len(bwt_result)):
        if bwt_result[i] == bwt_result[i-1]:
            count += 1
        else:
            rle_result.append((bwt_result[i-1], count))
            count = 1
    
    # Append the last run
    rle_result.append((bwt_result[-1], count))
    
    return rle_result

# Example DNA sequence with gaps
sequence = """ agct """

# Perform BWT on the sequence
bwt_result = bwt_transform(sequence)

# Perform Run-Length Encoding (RLE) on the BWT result
rle_result = run_length_encoding(bwt_result)

# Output the results
print(f"BWT Result: {bwt_result}")
print(f"RLE Result: {rle_result}")
