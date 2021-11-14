# `setuptools_scm_azure_pipelines`

## Description

A stupidly simple [`setuptools_scm`](https://github.com/pypa/setuptools_scm) plugin that generates
 [PEP-440 post-releases](https://www.python.org/dev/peps/pep-0440/#toc-entry-8) packages versions prefixed
 with the Azure Pipelines `${BUILD_BUILDID}` for builds that happen on non-tagged git commits.

`BUILD_BUILID`, or rather `$(Build.BuildId)` in the Azure Pipeline lingo, is the variable that is set
by Azure Pipelines when a build is running.

When this variable is present and you are using this tool, your package's version will be:
- `{tag}`, e.g. `1.2.3` when you are building on a tag ("exact version"),
- `{tag}.post{BUILD_BUILDID}`, e.g. `1.2.3.post12345` when you are building an intermediate version ("on-commit"),

This allows your fellow developpers to get the "latest" version of a package, no matter what.

You might not want that to happen everytime, though. In that case, don't forget to pin you dependencies correctly using one of:
-   [`pip-tools`](https://github.com/jazzband/pip-tools)
-   [`Pipenv`](https://github.com/pypa/pipenv)
-   [`Poetry`](https://python-poetry.org/)

## Usage

### Usage in `pyproject.toml`

Set it up in `pyproject.toml` `[build-system]` section like this:

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm>=6.2", "setuptools_scm_azure_pipelines>=1.0"]

[tool.setuptools_scm]
local_scheme = "no-local-version"
version_scheme = "post-release-azure-build-id"
```
