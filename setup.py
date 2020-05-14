import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pyfull-py",
    version="0.0.1", #as of 14/05/2020
    author="Panudio",
    author_email="samuelkatz2245@gmail.com",
    description="A small package for random functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Samukat/pyfull",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
