from setuptools import find_packages, setup

setup(
    name='meteopipelib',
    packages=find_packages(include=['meteopipelib']),
    version='0.1.0',
    description='Client library for meteopipe based on paho mqtt',
    author='Marek Rośkowicz',
    url='https://github.com/rozek1997',
    license='MIT',
    install_requires=['paho-mqtt']
)
