from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name='Waifupy',
    version='2.0.0',
    license='MIT',
    author='Okimii',
    packages=find_packages('src/Waifupy'),
    package_dir={'': 'src'},
    url='https://github.com/Okimii/waifupy',
    keywords='waifu.pics python api wrapper ',
    install_requires=[
        'aiohttp'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)