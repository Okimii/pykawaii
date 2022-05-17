from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='pykawaii',
    version='2.0.0',
    license='MIT',
    author='Okimii',
    packages=find_packages('pykawaii'),
    package_dir={'': 'pykawaii'},
    url='https://github.com/Okimii/pykawaii',
    keywords='waifu.pics python api wrapper ',
    install_requires=[
        'aiohttp'
    ],
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown'
)