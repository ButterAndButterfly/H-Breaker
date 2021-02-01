import setuptools
import os
from head_breaker import version

with open("README.md", "r", encoding = 'utf-8') as fh:
    long_description  =  fh.read()

def find_packages(*tops):
    packages = []
    for d in tops:
        for root, dirs, files in os.walk(d, followlinks=True):
            if '__init__.py' in files:
                packages.append(root)
    return packages

setuptools.setup(
    name = "h-breaker",
    version = version.__version__,
    description = version.__descriptrion__,
    author = "NiceLee",
    author_email = "lijia0732@sina.com",
    license = "MIT",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ButterAndButterfly/H-breaker",
    zip_safe = True,
    packages = find_packages('head_breaker'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": ["h-breaker=head_breaker.main:main"]
    },
)
