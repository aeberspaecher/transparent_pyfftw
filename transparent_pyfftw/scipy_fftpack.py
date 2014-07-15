#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Wrappers for pyfftw's SciPy fftpack interfaces.
"""

import pyfftw.interfaces.scipy_fftpack as sfft

from .generate_wrappers import generate_wrapper
from .transparent_pyfftw import get_num_threads


# the wrappers are generated on import:
func_names = sfft.__all__

for func_name in func_names:
    num_threads = get_num_threads()
    original_docstring = sfft.__dict__[func_name].__doc__
    wrapper_func_string = generate_wrapper(func_name, "scipy_fftpack",
                                           sfft.__dict__[func_name].__doc__,
                                           num_threads)

    # import pyfftw functions and add a '_' to the name:
    exec "from pyfftw.interfaces.scipy_fftpack import %s as _%s"%(2*(func_name,))

    # define the wrapper:
    exec wrapper_func_string
