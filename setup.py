import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyClassicRound",
    version="2.2",
    author="Rohit",
    author_email="rohit.shrivastava93@gmail.com",
    description="Current python 3's round function uses Banker's rounding, this package will help you to round off numbers the classical way.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohitxsh93/PyClassicRound",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)