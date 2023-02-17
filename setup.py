from setuptools import setup, find_packages
from version import __safe_version__

with open("./requirements.txt", "r") as f:
    requirements = f.read().strip().split("\n")


setup(
    name="foobar",
    version=__safe_version__,
    packages=find_packages(),
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        foobar=__init__:foobar_cli
    """,
)
