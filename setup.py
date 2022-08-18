from setuptools import find_packages
from setuptools import setup


setup(
    name='pre-commit-terraform',
    description='Pre-commit checks',
    url='https://github.com/forestnd/pre-commit-checks',
    version_format='{tag}+{gitsha}',

    author='Contributors',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'setuptools-git-version',
    ],
    entry_points={
        'console_scripts': [
            'trailing-whitespace-fixer= hooks.trailing_whitespace_fixer:main',
            'detect-aws-credentials= hooks.detect_aws_credentials:main',
            'detect-private-key= hooks.detect_private_key:main',
            'check-added-large-files= hooks.check_added_large_files:main',
            'double-quote-string-fixer = hooks.string_fixer:main',
            'check-json= hooks.check_json:main'
        ],
    },
)
