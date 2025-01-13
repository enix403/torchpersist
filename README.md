# torchpersist
A caching decorator for PyTorch computations.

# torchpersist

`torchpersist` is a Python library that provides a caching decorator for PyTorch computations. It simplifies saving and loading results of expensive function calls to and from disk and prevents redundant computations.

## Installation

```bash
git clone https://github.com/enix403/torchpersist.git
cd torchpersist
pip install .
```

## Usage

Decorate your PyTorch function with the `@torchpersist(...)` decorator and specify the path where the results should be cached.

```python
import torch
from torchpersist import torchpersist

@torchpersist("saved.pt")
def generate_tensor(scale: float):
  return torch.rand((2, 5))
```
