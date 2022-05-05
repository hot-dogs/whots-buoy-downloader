from setuptools import setup, find_packages

setup(
    name='whots-buoy-downloader',
    version='0.0.1',
    extras_require={
        'tests': ['pytest'],
        'roman': ['roman>=3.3'],
    },
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    author='Fernando Carvalho Pacheco',
    author_email='fernando.pacheco@hawaii.edu',
    description='WHOTS file downloader is  responsible for downloading the WHOTS text file and writing it to disk.',
)
