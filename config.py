import os
from math import *

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024  # 1MB upload limit
    ALLOWED_EQUATION_CHARS = set('0123456789xy+-*/.()^ ')
    ALLOWED_FUNCTIONS = {
        'sin': sin, 'cos': cos, 'tan': tan,
        'exp': exp, 'log': log, 'sqrt': sqrt,
        'pi': pi, 'e': e
    }