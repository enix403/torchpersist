import os
from functools import wraps

import torch

def torchpersist(path: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.path.exists(path):
                return torch.load(path, weights_only=True)
            else:
                result = func(*args, **kwargs)
                torch.save(result, path)
                return result
        return wrapper
    return decorator
