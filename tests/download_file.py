import pytest

from pygithubctl.pygithubctl import download_file


def test_download_file_attribute_error():
    with pytest.raises(AttributeError, match=r".* object has no attribute .*"):
        download_file("repository", "sha", "source", "target")