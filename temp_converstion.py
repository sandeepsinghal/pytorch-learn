# celcius to fahrenheit conversion using PyTorch
"""
This script performs Celsius to Fahrenheit temperature conversion using PyTorch tensors.
Formula used:
    Fahrenheit = Celsius * 1.8 + 32
Variables:
    b  : torch.tensor
        The bias term representing the freezing point of water in Fahrenheit (32°F).
    w1 : torch.tensor
        The weight term representing the scaling factor for Celsius to Fahrenheit conversion (1.8).
    X1 : torch.tensor
        Input tensor containing temperatures in Celsius.
The script computes the predicted Fahrenheit values (y_pred) for the given Celsius inputs using the formula above.
"""
import torch

b = torch.tensor(32)

w1 = torch.tensor(1.8)

X1 = torch.tensor([0, 36.5, 50])

y_pred = w1 * X1 + b
print(y_pred)  # Output the predicted values
