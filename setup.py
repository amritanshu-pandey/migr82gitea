#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'requests',
    'GitPython',
]

setup_requirements = ['pytest-runner', ]

test_requirements = [
        'pytest>=3',
        'flake8',
        'mypy'
    ]

setup(
    author="Amritanshu Pandey",
    author_email='email@amritanshu.in',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Program to one way sync git repositories between supported git servers",
    entry_points={
        'console_scripts': [
            'migr82gitea=migr82gitea.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='migr82gitea',
    name='migr82gitea',
    packages=find_packages(include=['migr82gitea', 'migr82gitea.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    extras_require={
            'test': test_requirements
        },
    url='https://github.com/amritanshu-pandey/migr82gitea',
    version='0.1.0',
    zip_safe=False,
)
