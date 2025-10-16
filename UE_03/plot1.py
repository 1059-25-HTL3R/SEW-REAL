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

#makierung bei sin((2*pi)/2)
wert = (2 * np.pi) / 3
plt.plot([wert, wert], [0, np.cos(wert)], color='blue', linewidth=2.5, linestyle="--")
plt.plot([wert, wert], [0, np.sin(wert)], color='red', linewidth=2.5, linestyle="--")

#punktbeschriftung
plt.annotate(r'$\sin(\frac{2\pi}{3})$',
             xy=(wert, np.sin(wert)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate(r'$\cos(\frac{2\pi}{3})$',
             xy=(wert, np.cos(wert)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Beschriftung hervorheben
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

# Layout
plt.tight_layout()
plt.show()
