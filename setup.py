from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='pynse',
    version='0.1',
    packages=['pynse'],
    url='https://github.com/anoopjangra',
    license='',
    author='Anoop Jangra',
    author_email='anoopjangra@gmail.com',
    description='Library to extract realtime and historical data from NSE website',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['requests', 'fake-headers', 'bs4', 'pandas','beautifulsoup4'],
    classifiers=[
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],)
