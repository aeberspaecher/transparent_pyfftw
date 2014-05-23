#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""An attempt at the most transparent pyfftw wrapper possible.

The goal of this module is to make using PYFFTW as much a no-brainer as it was
with the dying anfft project. Hide "boring" stuff such as caching, SIMD
alignment and threads form the user.
"""

import pyfftw
from pyfftw.interfaces.numpy_fft import fft as pfft, ifft as pifft, fft2 as pfft2, \
    ifft2 as pifft2, fftn as pfftn, ifftn as pifftn, \
    rfft as prfft, irfft as pirfft, hfft as phfft, ihfft as pihfft, \
    rfft2 as prfft2, irfft2 as pirfft2, rfftn as prfftn, irfftn as pirfftn, \
    fftshift, ifftshift, fftfreq

from .options import pyfftw_threads, wisdom_file


def read_wisdom():
    """Read wisdom and get it in the data structures expected by pyfftw.
    """

    try:
        wisdom = file(wisdom_file, mode="r").readlines()
    except IOError:
        print("Wisdom file not loadable. If you haven't saved any wisdom yet, try calling save_wisdom().")
        wisdom = None
    else:
        if(len(wisdom) == 0):
            print("Wisdom file is empty. Try calling save_wisdom().")
            wisdom = None
        else:
            # FIXME: glue together suitable strings before importing
            wisdom_tuple = []
            for line in wisdom:
                # if a line starts with a space, it belongs to last list member
                # ("current" element). otherwise, it starts a new member
                if(line.startswith(" ") or line.startswith(")")):
                    wisdom_tuple[-1] += line  # append to string
                else:
                    wisdom_tuple.append(line)

            wisdom = wisdom_tuple  # override

    return wisdom


# if configured to use centuries of fftw wisdom, read the fftw oracle of delphi:
if(wisdom_file is not None):
    wisdom = read_wisdom()
    if(wisdom is not None):
        pyfftw.import_wisdom(wisdom)

pyfftw_simd_alignment = pyfftw.simd_alignment
pyfftw.interfaces.cache.enable()
pyfftw.interfaces.cache.set_keepalive_time(300)  # keep cache alive for 300 sec
# TODO: make this a configurable parameter?


def save_wisdom():
    """Save generated wisdom to file specified when configuring the project.
    """

    if(wisdom_file is not None):
        wisdom = pyfftw.export_wisdom()
        with file(wisdom_file, mode="w") as f:
            for wisdom_bit in wisdom:
                f.write(wisdom_bit)
    else:
        raise Exception("Configured not to use any FFTW wisdom!")


def get_empty_fftw_array(shape, dtype="float64", *kwargs):
    """Create memory aligned empty array.
    """

    return pyfftw.n_byte_align_empty(shape, pyfftw_simd_alignment, dtype, **kwargs)


def align_array(arr):
    """Return memory aligned copy of arr. This may be speed pyfftw calls up.
    """

    return pyfftw.n_byte_align(arr, pyfftw_simd_alignment)


def fft(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.fft.
    """

    kwargs["threads"] = pyfftw_threads

    return pfft(*args, **kwargs)


def ifft(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.ifft.
    """

    kwargs["threads"] = pyfftw_threads

    return pifft(*args, **kwargs)


def fft2(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.fft2.
    """

    kwargs["threads"] = pyfftw_threads

    return pfft2(*args, **kwargs)


def ifft2(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.ifft2.
    """

    kwargs["threads"] = pyfftw_threads

    return pifft2(*args, **kwargs)


def fftn(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.fftn.
    """

    kwargs["threads"] = pyfftw_threads

    return pfftn(*args, **kwargs)


def ifftn(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.ifftn.
    """

    kwargs["threads"] = pyfftw_threads

    return pifftn(*args, **kwargs)


def rfft(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.rfft.
    """

    kwargs["threads"] = pyfftw_threads

    return prfft(*args, **kwargs)


def irfft(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.irfft.
    """

    kwargs["threads"] = pyfftw_threads

    return pirfft(*args, **kwargs)


def rfft2(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.rfft2.
    """

    kwargs["threads"] = pyfftw_threads

    return prfft2(*args, **kwargs)


def irfft2(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.irfft2.
    """

    kwargs["threads"] = pyfftw_threads

    return pirfft2(*args, **kwargs)


def rfftn(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.rfftn.
    """

    kwargs["threads"] = pyfftw_threads

    return prfftn(*args, **kwargs)


def irfftn(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.irfftn.
    """

    kwargs["threads"] = pyfftw_threads

    return pirfftn(*args, **kwargs)


def hfft(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.hfft.
    """

    kwargs["threads"] = pyfftw_threads

    return phfft(*args, **kwargs)


def ihfft(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.ihfft.
    """

    kwargs["threads"] = pyfftw_threads

    return pihfft(*args, **kwargs)


def hfft2(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.hfft2.
    """

    kwargs["threads"] = pyfftw_threads

    return phfft2(*args, **kwargs)


def ihfft2(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.ihfft2.
    """

    kwargs["threads"] = pyfftw_threads

    return pihfft2(*args, **kwargs)


def hfftn(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.hfftn.
    """

    kwargs["threads"] = pyfftw_threads

    return phfftn(*args, **kwargs)


def ihfftn(*args, **kwargs):
    """Wrapper for pyfftw.interfaces.numpy_fft.ihfftn.
    """

    kwargs["threads"] = pyfftw_threads

    return pihfftn(*args, **kwargs)
