def avalanche_effect(original_output, modified_output):
    """Compute the Avalanche Effect between two binary outputs."""
    # Ensure both outputs are of the same length
    assert len(original_output) == len(modified_output), "Outputs must have the same length."

    # Count the differing bits
    differing_bits = sum(1 for a, b in zip(original_output, modified_output) if a != b)

    return (differing_bits / len(original_output)) * 100

def ber(original_bits, received_bits):
    """Compute the Bit Error Rate between original and received bit sequences."""
    # Ensure both bit sequences are of the same length
    assert len(original_bits) == len(received_bits), "Bit sequences must have the same length."

    # Count the erroneous bits
    erroneous_bits = sum(1 for a, b in zip(original_bits, received_bits) if a != b)

    return erroneous_bits / len(original_bits)

def generate_Key(key_32chars):
    if len(list(key_32chars))!=32:
        raise ValueError(f"Key must have 32 chars exactly. It has {len(key_32chars)} chars")

    key = ""
    for char in key_32chars:
        byte = format(ord(char),'08b')
        key += byte
    return key






