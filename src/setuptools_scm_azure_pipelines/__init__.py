from os import getenv

from setuptools_scm.version import ScmVersion  # type: ignore


def postrelease_azure_build_id(version: ScmVersion) -> str:
    if version.exact:
        return f'{version.tag}'
    else:
        return f'{version.tag}.post{getenv("BUILD_BUILDID", version.distance)}'
