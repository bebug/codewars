def last_survivor(letters: str, coords: []):
    for n in coords:
        letters = letters[:n] + letters[n+1:]
    return letters