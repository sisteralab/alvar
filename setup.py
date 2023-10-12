from setuptools import setup, find_packages
from io import open


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


setup(
    name="alvar",
    version="0.1",
    description="Allan variance calculation",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="yarvod",
    author_email="yar.vod.ole@gmail.com",
    url="https://github.com/sisteralab/alvar",
    keywords="allan variance",
    packages=find_packages(),
    requires=["numpy==1.26.0"]
)
