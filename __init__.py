#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Transparent wrappers for pyfftw's NumPy FFT interfaces.

Does nothing more but inserting a number of threads into your fft calls and
handing that parameter to pyfftw.

List of wrapped functions:
fft, ifft, fft2, ifft2, fftn, ifftn, rfft, irfft, rfft2, irfft2, rfftn, irfftn,
hfft, ihfft, hfft2, ihfft2, hfftn, ihfftn

To save acquired wisdom, call save_wisdom(). Wisdom is automatically loaded on
import.
"""


from transparent_pyfftw import *
