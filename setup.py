from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='od_aws_iot_admin',
    version='0.0.1',
    description='OculusD AWS IoT Admin Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.oculusd.com/',
    author='OculusD',
    author_email='info@oculusd.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='cli library iot oculusd',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['boto3'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://www.oculusd.com/',
        'Funding': 'https://www.oculusd.com/',
        'Say Thanks!': 'https://www.oculusd.com/',
        'Source': 'https://www.oculusd.com/',
    },
)
