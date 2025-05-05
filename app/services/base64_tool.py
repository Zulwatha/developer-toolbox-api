import base64

def encode_to_base64(text: str) -> str:
    # Encodes the input string to Base64
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")

def decode_from_base64(b64_string: str) -> str:
    # Decodes Base64 back to original string
    try:
        decoded = base64.b64decode(b64_string)
        return decoded.decode("utf-8")
    except Exception as e:
        raise ValueError("Invalid Base64 input.")
