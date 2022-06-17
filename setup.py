import re
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('src/lingvo_dictionary/__init__.py', 'r') as f:
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
    url='https://github.com/Korolev-Oleg/lingvo-dictionary',
    license='MIT',
    keywords=['lingvo', 'dictionary', 'dictionaries', 'lingvo-api'],
    description='Python library for work with ABBYY Lingvo Dictionaries API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/Korolev-Oleg/lingvo-dictionary/issues",
        "Documentation": "https://developers.lingvolive.com/en-us/Help",
        "Developer Telegram": "https://t.me/hustncn"
    },
    install_requires=[
        'requests>=2.28'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
)
