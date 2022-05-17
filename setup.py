from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name='waifpy',
    version='2.0.0',
    license='MIT',
    author='Okimii',
    packages=find_packages('waifpy'),
    package_dir={'': 'Waifpy'},
    url='https://github.com/Okimii/waifpy',
    keywords='waifu.pics python api wrapper ',
    install_requires=[
        'aiohttp'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)