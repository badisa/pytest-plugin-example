import re
import ast

from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('explugin/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode(
        'utf-8')).group(1)))

setup(
    name='Pytest Plugin',
    version=version,
    packages=find_packages(),
    url='http://www.github.com/badisa',
    author='Forrest York',
    entry_points={
        'pytest11': ['customplugin = explugin.plugin']
    },
    long_description=open('README.rst').read(),
    zip_safe=False,
    license='Other/Proprietary License',
    include_package_data=True,
    install_requires=[
        'pytest'
    ],
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ]
)
