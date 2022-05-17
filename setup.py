from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name='waifupics',
    version='2.0.0',
    license='MIT',
    author='Okimii',
    packages=find_packages('waifupics'),
    package_dir={'': 'Waifupics'},
    url='https://github.com/Okimii/waifupics',
    keywords='waifu.pics python api wrapper ',
    install_requires=[
        'aiohttp'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)