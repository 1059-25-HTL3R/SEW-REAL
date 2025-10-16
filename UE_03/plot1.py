import numpy as np
import matplotlib.pyplot as plt

# Daten
x = np.linspace(-np.pi , np.pi, 800)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots()

# Plot
plt.plot(x, y_cos, color="blue", linewidth=2, label="Cosinus")
plt.plot(x, y_sin, color="red", linewidth=2, label="Sinus")

# Layout
plt.tight_layout()
plt.show()