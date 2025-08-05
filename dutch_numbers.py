ONES: dict[str, str] = {
    "0": "nul",
    "1": "één",
    "2": "twee",
    "3": "drie",
    "4": "vier",
    "5": "vijf",
    "6": "zes",
    "7": "zeven",
    "8": "acht",
    "9": "negen",
}
ONE_NO_DIACRITICS = "een"
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
HUNDRED = "honderd"

VOWELS: list[str] = ["a", "e", "i", "o", "u"]
AND_AFTER_VOWEL = "ën"
AND_AFTER_CONSONANT = "en"

def proc_one_to_ninety_nine(n: int) -> str:
    if 0 <= n <= 9:
        return ONES[str(n)]
    elif 11 <= n <= 19:
        return TEENS[str(n)]
    elif 10 <= n <= 99:
        tens_digit, ones_digit = str(n)
        if ones_digit == "0":
            return TENS[tens_digit]
        else:
            ones = ONES[ones_digit]
            if ones == "één":
                ones = ONE_NO_DIACRITICS
            if ones[-1] in VOWELS:
                en = AND_AFTER_VOWEL
            else:
                en = AND_AFTER_CONSONANT
            return f"{ones}{en}{TENS[tens_digit]}"
    raise Exception(f"(0-99) Invalid input : {n}")

def proc_hundreds_digit(hundreds_digit: str) -> str:
    if hundreds_digit == "1":
        return HUNDRED
    elif hundreds_digit in ONES:
        return ONES[hundreds_digit] + HUNDRED
    raise Exception(f"(100s) Invalid input : {hundreds_digit}")

def proc_to_999(n: int) -> str:
    if 0 <= n <= 99:
        return proc_one_to_ninety_nine(n)
    elif 100 <= n <= 999:
        hundreds_digit, tens_digit, ones_digit = str(n)
        if tens_digit == "0" and ones_digit == "0":
            return proc_hundreds_digit(hundreds_digit)
        else:
            hundreds = proc_hundreds_digit(hundreds_digit)
            tens_and_ones = proc_one_to_ninety_nine(int(tens_digit + ones_digit))
            return hundreds + tens_and_ones
    raise Exception(f"(0-999) Invalid input : {n}")

def num_to_words(n: int) -> str:
    if 0 <= n <= 999:
        return proc_to_999(n)
    return "?"

for i in range(0, 1000):
    print(i, num_to_words(i))