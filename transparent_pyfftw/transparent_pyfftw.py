#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Common functions for transparent_pyfftw.
"""

import os

import numpy as np

import pyfftw

from .options import wisdom_file


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
            wisdom_tuple = []
            for line in wisdom:
                # if a line starts with a space or a right paren, it belongs to
                # last list member ("current" element). otherwise, it starts a
                # new member.
                if(line.startswith(" ") or line.startswith(")")):
                    wisdom_tuple[-1] += line  # append to string
                else:
                    wisdom_tuple.append(line)

            wisdom = wisdom_tuple  # override

    return wisdom


# if configured to use centuries of fftw wisdom, read the fftw oracle of
# delphi (i.e. the wisdom file) - do this on import:
if(wisdom_file is not None):
    wisdom = read_wisdom()
    if(wisdom is not None):
        pyfftw.import_wisdom(wisdom)

pyfftw_simd_alignment = pyfftw.simd_alignment
pyfftw.interfaces.cache.enable()
pyfftw.interfaces.cache.set_keepalive_time(300)  # keep cache alive for 300 sec
# TODO: make this a configurable parameter?


def get_num_threads():
    """Get number of threads from environment variable.

    Returns
    -------
    num_threads : int
        $TFFTW_NUM_THREADS if set, 1 otherwise.
    """

    # set number of threads from environment variable:
    try:
        num_threads = int(os.environ["TFFTW_NUM_THREADS"])
    except KeyError:
        num_threads = 1

    return num_threads


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


def get_empty_fftw_array(shape, dtype=np.float64, **kwargs):
    """Create memory aligned empty array.

    Parameters
    ----------
    shape : tuple-like
    dtype : object

    Returns
    -------
    aligned : array
        Empty, byte-aligned array.

    Notes
    -----
    Keyword arguments are passed on to pyfftw.n_byte_align_empty().
    """

    return pyfftw.n_byte_align_empty(shape, pyfftw_simd_alignment, dtype, **kwargs)


def align_array(arr):
    """Return memory aligned copy of arr. This may be speed up pyfftw calls.

    Parameters
    ----------
    arr : array

    Returns
    -------
    arr_aligned : array
    """

    return pyfftw.n_byte_align(arr, pyfftw_simd_alignment)
