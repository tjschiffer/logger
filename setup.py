import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logger",
    version="0.1.dev1",
    author="T.J. Schiffer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tjschiffer/logger",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
