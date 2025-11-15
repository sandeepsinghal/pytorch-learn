# celcius to fahrenheit conversion using PyTorch

import torch

b = torch.tensor(32)

w1 = torch.tensor(1.8)

X1 = torch.tensor([0, 36.5, 50])

y_pred = w1 * X1 + b
print(y_pred)  # Output the predicted values
