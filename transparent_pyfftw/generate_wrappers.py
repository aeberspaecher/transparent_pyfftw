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

def generate_wrapper(name, module, original_docstring):
    """Generate a wrapper function.

    Parameters
    ----------
    name : string
        Name of the function wrapped.
    module : string
        Name of the module the wrapped function is part of.
    original_docstring : string
        Docstring of the wrapped function.

    Returns
    -------
    wrapper_code : string
        A string that contains the code to the wrapper function.
    """

    # create a string that informs the user about the 'threads' parameter added
    # to the call if appropriate:
    add_keyword_atom = "additional arguments docs"
    additional_arg_string = "Arguments automatically added on call are 'threads=pyfftw_threads'.\n" if add_keyword_atom in original_docstring else "This wrapper does nothing but to call the pyfftw function.\n"
    wrapper_string = '''
def %(name)s(*args, **kwargs):
    """A thin wrapper around pyfftw.interfaces.%(module)s.%(name)s.

    %(additional_arg_string)s
    Docstring of original pyfftw function:
    --------------------------------------
    %(original_docstring)s
    """

    kwargs["threads"] = pyfftw_threads

    return _%(name)s(*args, **kwargs)
'''%locals()

    return wrapper_string


# TODO: method to decide which wrappers (in Scipy) can take a threads argument
# (probably relying on pyfftw's documentation works: if <interfaces_additional_args>
# is in the doctsring, we can add the threads keyword)
