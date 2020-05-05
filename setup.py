import os
import setuptools

version = {}
with open('museful/version.py') as f:
    exec(f.read(), version)

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name="museful",
    version=version['__version__'],
    author="Ondřej Cífka",
    description="Symbolic music processing utilities",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pretty_midi',
    ],
)
