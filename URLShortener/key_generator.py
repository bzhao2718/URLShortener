
import string
import random
from abc import ABC, abstractmethod
from .DaoUtil import is_url_key_exsits

def generate_random_key(key_len = 7):
    random_key = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(key_len)])
    return random_key

class AbstractGenerator(ABC):

    @abstractmethod
    def generate_unique_key(self, key_len=7):
        pass

class RandomKeyGenerator(AbstractGenerator):
    """Generate a random letters and digits combination with length specified by :key_len"""
    def generate_unique_key(self, key_len=7):
        unique_key = generate_random_key()
        while is_url_key_exsits(unique_key):
            unique_key = generate_random_key()
        return unique_key

class Base62KeyConversionGenerator(AbstractGenerator):
    """Generate a letters and digits combination by converting a hashvalue into base 62 with length specified by :key_len"""
    def generate_unique_key(self, key_len=7):
        """TODO"""
        pass

def key_generator_factory(strategy="random"):
    generators={
        'random':RandomKeyGenerator(),
        'base62':Base62KeyConversionGenerator()
    }
    return generators[strategy]

# def generate_unique_key(key_len = 7):
#     """Generate a random letters and digits combination with length specified by :key_len"""
#     unique_key = generate_random_key()
#     while is_url_key_exsits(unique_key):
#         unique_key = generate_random_key()
#     return unique_key




