#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Generate pyfftw wrapper functions by name.

Add the threads keyword to the call, do nothing else.
"""

names = ["fft", "ifft", "fft2", "ifft2", "fftn", "ifftn", "rfft", "irfft",
         "rfft2", "irfft2", "rfftn", "irfftn", "hfft", "ihfft", "hfft2",
         "ihfft2", "hfftn", "ihfftn"]

generate_wrapper = lambda name: '''
def %s(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.%s.
    """

    kwargs["threads"] = pyfftw_threads

    return p%s(*args, **kwargs)
'''%(3*(name,))

for name in names:
    print generate_wrapper(name)
