The simple minded pyfftw wrapper
================================

Intro
-----

The Fastet Fourier Transform in the West is an incredible library. There are at
least two different Python wrappers around FFTW: anfft (which is declared dead)
and pyfftw.

anfft used to be the simplest posssible wrapper possible. It automatically took
care of FFTW's 'wisdom' (recipes on how to compute specific transforms the
fastest) and used threads if possible. From a user's point of view, it hid all
FFTW details a simple minded user does not want to take care of. As the only
downside it didn't expose the full range of possible routines, e.g. a dedicated
fft2() was missing.

pyfftw is the more complete wrapper. These days, it even offers NumPy or SciPy
style interfaces to FFTW. However, it also exposes FFTW details such as wisdom,
threads and buffers. This wrapper of a wrapper tries to hide these details much
in the spirit of anfft.

Configuring and installing
--------------------------

The only time the user needs to think about wisdom and threads is when
preparing to install. Configure first::

    ./waf configure --num-threads=2 --wisdom-file="/home/your_user/.pyfftw_wisdom"

Set ``--num-threads=1`` in case your pyfftw does not support threads.

Last, install with

::

    sudo ./waf install


Usage
-----

Just use the wrapper like this

::

    import transparent_pyfftw_wrapper as tfft

    ...

    tfft.fft2(your_data)

When performing new transforms, pyfftw will acquire new wisdom - to use this
wisdom in the future, call ``tfft.save_wisdom()``. Wisdom is automatically
loaded when the wrapper is imported.

Optionally making your project depend on transparent_pyfftw_wrapper
-------------------------------------------------------------------

In case you want to use transparent_pyfftw_wrapper in your project without
having it as a hard dependency for users, you may use the fact that pyfftw and
thus this wrapper as well use NumPy interfaces::

    try:
        from transparent_pyfftw_wrapper import fft, ifft
    except ImportError:
        from numpy.fft import fft, ifft


License and Copyright
---------------------

Copyright 2014 by Alexander Eberspächer

BSD license, see LICENSE file
