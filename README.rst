The simple minded pyfftw wrapper
================================

Intro
-----

The Fastet Fourier Transform in the West is an incredible library. There are at
least two different Python wrappers around FFTW: `anfft <http://www>`_ (which
is declared dead) and the awesome `pyfftw <http://www>`_.

anfft used to be the simplest posssible wrapper possible. It automatically took
care of FFTW's 'wisdom' (recipes on how to compute specific transforms the
fastest) and used threads if possible. From a user's point of view, it hid all
FFTW details a simple minded user does not want to take care of. As the only
downside it didn't expose the full range of possible routines, e.g. a dedicated
fft2() was missing.

pyfftw is the more complete wrapper. These days, it even offers `NumPy or SciPy
style interfaces <http://>`_to FFTW. However, it also exposes FFTW details such
as wisdom, threads and buffers. This wrapper of a wrapper tries to hide these
details much in the spirit of anfft.

Configuring and installing
--------------------------

The only time the user needs to think about wisdom files is when preparing to
install. Configure first::

    ./waf configure --wisdom-file="/home/your_user/.pyfftw_wisdom"

The number of threads used is determined by an environment variable.
Set (using bash)

::

    export -x TFFTW_NUM_THREADS=2

to use two threads. If your FFTW does not support threads, do not set this
variable or set it to 1. If the variable is unset, a single thread is used.

Last, install with

::

    sudo ./waf install


Usage
-----

Both the NumPy and Scipy style interfaces from pyfttw are supported. Import one
of those using::

    import transparent_pyfftw.numpy_fft as nftt
    import transparent_pyfftw.scipy_fftpack as sftt

In each case, just use this package as if you had used the NumPy FFTs or the
Scipy ones::

    nfft.fft2(your_data)

When performing new transforms, pyfftw will acquire new wisdom - to use this
wisdom in the future, call ``transparent_pyfftw.save_wisdom()``. Wisdom is
automatically loaded when the wrapper is imported.

To create a byte-aligned array, call

::

    foo = transparent_pyfftw.get_empty_fftw_array([256, 512])  # create a 256 x 512 array


Optionally making your project depend on transparent_pyfftw_wrapper
-------------------------------------------------------------------

In case you want to use transparent_pyfftw_wrapper in your project without
having it as a hard dependency for users, you may use the fact that pyfftw and
thus this wrapper as well use NumPy interfaces::

    try:
        from transparent_pyfftw_wrapper.numpy_fft import fft, ifft
    except ImportError:
        from numpy.fft import fft, ifft


License and Copyright
---------------------

Copyright 2014 by Alexander Eberspächer

BSD license, see LICENSE file
