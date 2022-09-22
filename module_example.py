def _strip_punctuation(sentence):
    """Strips punctuation and all whitespace off the end of a sentence"""

    return sentence.strip().rstrip("!.")


def piratify(str):
    """Generic piratify of whole paragraphs, by exclaiming everything!"""

    return (str + " ").replace(". ", "! ").replace(".\n", "!\n").strip()


def me_hearties(str):
    """Appends 'me hearties!' to the end of a stub sentence"""

    stub = _strip_punctuation(str)

    return stub.strip() + ", me hearties! "


def yarr(str):
    """Appends 'Yarr' to the start of a stub sentence and piratifies it"""

    stub = _strip_punctuation(str)

    return "Yarr, " + stub[0].lower() + stub[1:] + "! "
