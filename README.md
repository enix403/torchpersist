# torchpersist
A decorator for caching PyTorch computations.

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
