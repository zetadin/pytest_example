#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Examples of how to use pytest.

    Run `pytest` to execute tests on all the functions
    in all the .py files in the current folder.
"""

import numpy as np
import os
import pytest
from numpy.testing import assert_almost_equal

def test_add():
    """Example test function taking no arguments.

        Use `assert` or `raise` errors to indicate that things are broken.
        These can also originate in functions called from here.
        `pytest` will give a detailed backtrace, including surrounding code.
        
    """
    a = 1;
    b = 1;
    c = a+b;
    assert(c==2);
    if(not isinstance(c, float)): #this test will fail
        raise TypeError(str(type(c))+" encountered instead of float");


@pytest.mark.parametrize("a, b", [
    (3.,  1.),
    (5., -1.)
])
def test_add2(a,b):
    """Example test function taking some arguments.
    
    Use `@pytest.mark.parametrize` to specify multiple
    sets of arguments.
    
    Numpy's `assert_almost_equal` lets you check if values are
    approximately equal.

    Args:
        a (float): The first parameter.
        b (float): The second parameter.

    """
    assert_almost_equal(a+b, 4.0, decimal=5);
    


def test_temp_files(tmpdir):
    """Example function creating temporary files.
    More examples and functionality for temp files can be found
    [here](http://doc.pytest.org/en/latest/tmpdir.html).

    Args:
        tmpdir (py.path.local): unique temporary folder atomatically
            provided by `pytest` for current test function.
            These are only kept for three runs of `pytest`.
    """
    orig_dir = os.getcwd()
    os.chdir(tmpdir)
    
    o = np.random.random(10);
    fh = tmpdir.join("test.dat")
    np.savetxt(fh, o)
    
    i = np.loadtxt(str(tmpdir)+"/test.dat")
    
    os.chdir(orig_dir)   #reset cwd, this might not be needed
    
    assert(np.array_equal(o,i));
    
    
    