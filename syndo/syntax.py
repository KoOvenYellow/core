def syntax_vector(sentence: str) -> np.ndarray:
    """
    Generate a syntax vector from a sentence.
    Filters out non-printable characters.
    """
    vector = np.array([ord(c) for c in sentence if c.isprintable()])[:10]
