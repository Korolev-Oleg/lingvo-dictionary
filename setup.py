import re
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('src/lingvo_api/__init__.py', 'r') as f:
    version = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]+)[\'"]',
        f.read(),
        re.MULTILINE
    ).group(1)

setup(
    name='lingvo-dictionary',
    author='korolev-oleg',
    author_email='ok@hustn.cn',
    version=version,
    url='',
    license='MIT',
    keywords=['lingvo', 'dictionary', 'dictionaries', 'lingvo-api'],
    description='Python library for work with ABBYY Lingvo Dictionaries API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
)
