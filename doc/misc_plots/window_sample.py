import numpy as np
from scipy.signal import gaussian
import matplotlib.pyplot as plt

signal = np.random.randn(256)
window = gaussian(256, 10)
plt.subplot(211)
plt.plot(np.arange(256), signal, "g", label="signal")
plt.plot(np.arange(256), window, "r", label="window")
plt.xlim(0, 256)
plt.legend()
plt.subplot(212)
plt.plot(np.arange(256), signal * window)
plt.xlim(0, 256)
plt.title("Windowed signal")
plt.show()
