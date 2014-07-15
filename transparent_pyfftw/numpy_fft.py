#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Wrappers for pyfftw's NumPy fft interfaces.
"""

import pyfftw.interfaces.numpy_fft as nfft

from .generate_wrappers import generate_wrapper
from .transparent_pyfftw import *


# the wrappers are generated on import:
func_names = nfft.__all__

for func_name in func_names:
    num_threads = get_num_threads()
    original_docstring = nfft.__dict__[func_name].__doc__
    wrapper_func_string = generate_wrapper(func_name, "numpy_fft",
                                           nfft.__dict__[func_name].__doc__,
                                           num_threads)

    # import pyfftw functions and add a '_' to the name:
    exec "from pyfftw.interfaces.numpy_fft import %s as _%s"%(2*(func_name,))

    # define the wrapper:
    exec wrapper_func_string
