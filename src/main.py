import random
import string
import nltk
from typing import List, Optional


def pin_generator(length: int = 8) -> str:
    """
    Generate a random numeric PIN.
    """
    return ''.join([random.choice(string.digits) for _ in range(length)])


def randompass_generator(length: int = 8, symbols: bool = False, numbers: bool = False) -> str:
    """
    Generate a random password with customizable character sets.
    """
    password: str = string.ascii_letters
    if symbols:
        password += string.punctuation
    if numbers:
        password += string.digits
    return ''.join([random.choice(password) for _ in range(length)])


def memorablepass_generator(
        num_of_words: int = 4,
        separator: str = '-',
        vocabulary: Optional[List[str]] = None,
        capitalize: bool = False
) -> str:
    """
    Generate a memorable password using random words.
    """
    if vocabulary is None:
        try:
            vocabulary = nltk.corpus.words.words()
        except LookupError:
            nltk.download('words')
            vocabulary = nltk.corpus.words.words()
    password_words = [random.choice(vocabulary) for _ in range(num_of_words)]
    if capitalize:
        password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]

    return separator.join(password_words)            
