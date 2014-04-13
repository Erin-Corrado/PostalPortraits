import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires=['rauth']

setup(name='ContextIO v2.0 Client Library',
    version='1.1',
    description='Library for accessing the Context.IO API v2.0 in Python',
    long_description=README,
    author='Tony Blank, Jesse Dhillon',
    author_email='tony@context.io, jesse@deva0.net',
    url='http://context.io',
    keywords=['contextIO', 'dokdok', 'imap', 'oauth'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
