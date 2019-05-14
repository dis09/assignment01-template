from exercises import ex1
import numpy.random
import inspect
import pytest
from pytest import approx


x = numpy.random.normal(size=100)


@pytest.mark.mandatory
def test_modules():
    # tests if any external modules are imported
    assert len(inspect.getmembers(ex1, inspect.ismodule)) == 0


@pytest.mark.points(6)
def test_my_mean():
    assert ex1.my_mean(x) == approx(numpy.mean(x))


@pytest.mark.points(8)
def test_my_var():
    assert ex1.my_var(x) == approx(numpy.var(x), rel=1e-3)


@pytest.mark.points(10)
def test_my_median():
    assert ex1.my_median(x) == approx(numpy.median(x))


@pytest.mark.points(4)
def test_my_range():
    assert ex1.my_range(x) == approx(max(x)-min(x))


@pytest.mark.points(12)
def test_my_frequency_table():
    x = [1, 3, "hallo", 1, 1, 1, 3, 3, "hallo", "hallo", 1, "hallo", 3]
    counts = ex1.my_frequency_table(x)
    expected = {1: 5, 'hallo': 4, 3: 4}
    assert counts == expected
