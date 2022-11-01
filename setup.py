from importlib.util import find_spec
from setuptools import setup

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name='chest_simulator_package',
    version='0.0.1',
    author='Henrique SK',
    description='A random chests simulator',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/henrique-sk/chest_simulator_package',
    # packages=find_packages(),
    install_requires=[
        'requests',
        'importlib-metadata; python_version >= "3.5"',
    ],
)