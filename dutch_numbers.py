ONES: dict[str, str] = {
    "0": "nul",
    "1": "een",  # TODO één?
    "2": "twee",
    "3": "drie",
    "4": "vier",
    "5": "vijf",
    "6": "zes",
    "7": "zeven",
    "8": "acht",
    "9": "negen",
}
TENS: dict[str, str] = {
    "1": "tien",
    "2": "twintig",
    "3": "dertig",
    "4": "veertig",
    "5": "vijftig",
    "6": "zestig",
    "7": "zeventig",
    "8": "tachtig",
    "9": "negentig"
}
TEENS: dict[str, str] = {
    "11": "elf",
    "12": "twaalf",
    "13": "dertien",
    "14": "viertien",
    "15": "vijftien",
    "16": "zestien",
    "17": "zeventien",
    "18": "achttien",
    "19": "negentien"
}

def num_to_words(n: int) -> str:
    if 0 <= n <= 9:
        return ONES[str(n)]
    elif 11 <= n <= 19:
        return TEENS[str(n)]
    elif 10 <= n <= 99:
        tens, ones = str(n)
        if ones == "0":
            return TENS[tens]
        else:
            return f"{ONES[ones]}en{TENS[tens]}"
    return "?"

for i in range(0, 100):
    print(i, num_to_words(i))