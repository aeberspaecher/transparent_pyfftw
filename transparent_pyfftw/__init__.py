#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Transparent wrappers for pyfftw's NumPy FFT interfaces.

Does nothing more but inserting a number of threads into your FFT calls and
handing that parameter to pyfftw.

Wrappers are available for pyfftw.numpy_fft and pyfftw.scipy_fftpack.

To save acquired wisdom, call transparent_pyfftw.save_wisdom(). Wisdom is automatically loaded on import.

Additional helper functions: save_wisdom(), get_empty_fftw_array(),
align_array().
"""

from .transparent_pyfftw import *
