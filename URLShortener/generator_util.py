
import string
import random

from .DaoUtil import is_url_key_exsits

def generate_unique_key(key_len = 7):
    """Generate a random letters and digits combination with length specified by :key_len"""
    unique_key = generate_random_key()
    while is_url_key_exsits(unique_key):
        unique_key = generate_random_key()
    return unique_key

def generate_random_key(key_len = 7):
    random_key = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(key_len)])
    return random_key


