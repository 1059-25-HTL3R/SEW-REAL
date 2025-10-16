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

# Titel und Legende
plt.title("Zwettler")
plt.legend(loc="upper left")

#achsen
ax.spines['left'].set_position('center')   # y-Achse durch 0
ax.spines['bottom'].set_position('center') # x-Achse durch 0
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#achsenbeschriftung
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1,1],
        [r'$-1$', r'$+1$'])


# Layout
plt.tight_layout()
plt.show()