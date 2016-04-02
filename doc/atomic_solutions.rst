=====================================
Linear Time-Frequency Representations
=====================================

As seen in the previous sections, the Fourier transform alone is not adequate
for the analysis of nonstationary signals. We need solutions that are joint
variables of both time and frequency. The simplest of this class of solutions
are the *atomic* solutions, also known as linear time frequency
representations. The simplest representation in this class is the `Short time
Fourier Transform (STFT) <https://en.wikipedia.org/wiki/Short-time_Fourier_transform>`_.


Short Time Fourier Transform
----------------------------

In its simplest form, the STFT introduces time resolution into the Fourier
transform by dividing the signal into windows of time centered around a time
instant :math:`t`, and then applying the Fourier transform on these windows,
for each value of :math:`t`. Formally, it is defined as

	.. math::

	  F_{x}(t, \nu, h) = \int_{-\infty}^{\infty}x(u)h^{*}(u-t)e^{-j2\pi\nu u}du


where :math:`h(t)` is a short *time analysis window* centered around
:math:`t=0` and :math:`\nu=0`.

	.. plot:: misc_plots/window_sample.py

As shown in the figure, when a signal is *windowed* by a time analysis window
(which happens to be a Gaussian function in this case), the operation supresses
the signal outside the range of the window and amplifies the values at and
near the center. This allows us to express the total signal as a weighted sum
of elementary waveforms, also called "atoms". Each atom can be constructed from
the window function by translation in time and modulation in frequency.

	.. math::

 	  h_{t, \nu}(u) = h(u - t)e^{j2\pi\nu u}


Example: STFT on Speech
```````````````````````

In this example we shall load a speech sample (a recording of the word "GABOR") and perform STFT on it.


    >>> from scipy.io import loadmat
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # please change the following line as required.
    >>> DATA_PATH = join("doc", "_gallery", "data", "gabor.mat")
    >>> signal = loadmat(DATA_PATH)['gabor'].ravel()
    >>> tfr = loadmat(DATA_PATH)['tfr']
    >>> time = np.arange(338)
    >>> freq = np.arange(128, dtype=float) / 256.0 * 1000
    >>> dsp = np.fft.fftshift(np.abs(np.fft.fft(signal)) ** 2)

    >>> plt.subplot(211)
    >>> plt.plot(time, signal)
    >>> plt.subplot(212)
    >>> plt.plot(dsp)

    .. plot:: _gallery/plot_3_1_2_spectrum.py

From the plot of the signal and from its spectrum, it is not apparent which
part of the signal contrubutes to the peak at :math:`\approx 140 Hz`. Now,
let's see what the STFT reveals.

    >>> plt.contour(time, freq, tfr)

    .. plot:: _gallery/plot_3_1_2_stft.py

The first artifact in the signal, located at :math:`\approx` 150 Hz and between
25 ms and 75 ms, is the first syllable "GA", and the second, longer pattern
between 140 to 250 ms is the second syllable "BOR". The other patterns in the
TF representation are the harmonics of the original signal present at higher
frequencies. Handling harmonics is a crucial issue in the choice of
time-frequency representations, which we will deal with in greater detail in
the upcoming sections.


Time-Frequency Resolution of the STFT
-------------------------------------
