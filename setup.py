import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chocolate", # Replace with your own username
    version="0.0.2",
    author="Seungjae Ryan Lee",
    author_email="seungjaeryanlee@github.com",
    description="An improvement to Python's kwargs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seungjaeryanlee/chocolate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
