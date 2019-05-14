from exercises import ex2
import pytest
from pytest import approx


@pytest.mark.points(5)
def test_rows():
    assert ex2.n_rows == 40840


@pytest.mark.points(2.5)
def test_likes():
    assert ex2.max_likes == 4924056


@pytest.mark.points(2.5)
def test_dislikes():
    assert ex2.max_dislikes == 1470386


@pytest.mark.points(7.5)
def test_likes_title():
    assert ex2.max_likes_title == "BTS (방탄소년단) 'FAKE LOVE' Official MV"


@pytest.mark.points(7.5)
def test_dislikes_title():
    assert ex2.max_dislikes_title == 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind'


@pytest.mark.points(5)
def test_mean_views():
    assert ex2.mean_views == approx(603455, rel=1e-4)


@pytest.mark.points(5)
def test_median_views():
    assert ex2.median_views == 119277


@pytest.mark.points(10)
def test_corr_likes_views():
    assert ex2.corr_likes_views == approx(0.8242, rel=1e-2)


@pytest.mark.points(15)
def test_views_channel():
    assert ex2.max_views_channel == 'Marvel Entertainment'
