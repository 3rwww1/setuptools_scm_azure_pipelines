from unittest.mock import patch

from setuptools_scm.version import ScmVersion  # type: ignore

from setuptools_scm_azure_pipelines import postrelease_azure_build_id


def test_exact_without_env():
    version = ScmVersion(tag_version='1.2.3', distance=None)
    assert postrelease_azure_build_id(version) == '1.2.3'


def test_inexact_without_env():
    version = ScmVersion(tag_version='1.2.3', distance='abcdef')
    assert postrelease_azure_build_id(version) == '1.2.3.postabcdef'


def test_exact_with_env():
    version = ScmVersion(tag_version='1.2.3', distance=None)
    with patch.dict('os.environ', {'BUILD_BUILDID': '45678'}):
        assert postrelease_azure_build_id(version) == '1.2.3'


def test_inexact_with_env():
    version = ScmVersion(tag_version='1.2.3', distance='abcdef')
    with patch.dict('os.environ', {'BUILD_BUILDID': '45678'}):
        assert postrelease_azure_build_id(version) == '1.2.3.post45678'
