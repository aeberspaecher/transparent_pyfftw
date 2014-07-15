#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""Generate pyfftw wrapper functions by name.

Add the threads keyword to the call, do nothing else.
"""

# if the wrapper codes are removed from transparent_pyfftw_wrapper.py,
# we can regenerate and re-add with
# ./generate_wrappers.py >> transparent_pyfftw_wrapper.py

names = ["fft", "ifft", "fft2", "ifft2", "fftn", "ifftn", "rfft", "irfft",
         "rfft2", "irfft2", "rfftn", "irfftn", "hfft", "ihfft", "hfft2",
         "ihfft2", "hfftn", "ihfftn"]

def generate_wrapper(name, module, original_docstring, num_threads):
    """Generate a wrapper function.

    Parameters
    ----------
    name : string
        Name of the function wrapped.
    module : string
        Name of the module the wrapped function is part of.
    original_docstring : string
        Docstring of the wrapped function.
    num_threads : int
        Number of threads to use.

    Returns
    -------
    wrapper_code : string
        A string that contains the code to the wrapper function.
    """

    # create a string that informs the user about the 'threads' parameter added
    # to the call if appropriate:

    # check two versions of the string that triggers addition of the threads
    # keyword - this is necessary due to pyfftw documentation inconsistencies
    add_keyword_atoms = ('additional arguments docs', 'additional argument docs')
    if(any( [ keyword in original_docstring for keyword in add_keyword_atoms ] )):
        additional_arg_string = \
            'Arguments automatically added on call are "threads=%s".\n'%num_threads
        additional_arg_code = 'kwargs["threads"] = %s'%num_threads
    else:
        additional_arg_string = \
            'This wrapper does nothing besides calling the pyfftw function.\n'
        additional_arg_code = ''

    wrapper_string = '''
def %(name)s(*args, **kwargs):
    """A thin wrapper around pyfftw.interfaces.%(module)s.%(name)s.

    %(additional_arg_string)s
    Docstring of original pyfftw function:
    --------------------------------------
    %(original_docstring)s

    """
    %(additional_arg_code)s

    return _%(name)s(*args, **kwargs)
'''%locals()

    return wrapper_string
