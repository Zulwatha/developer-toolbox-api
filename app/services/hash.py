import hashlib

SUPPORTED_ALGOS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256
}

def generate_hash(text: str, algorithm: str) -> str:
    # Convert algorithm name to lowercase
    algorithm = algorithm.lower()

    # Check if algorithm is supported
    if algorithm not in SUPPORTED_ALGOS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    # Get the appropriate hash function
    hash_func = SUPPORTED_ALGOS[algorithm]()
    hash_func.update(text.encode("utf-8"))

    # Return hexadecimal digest
    return hash_func.hexdigest()
