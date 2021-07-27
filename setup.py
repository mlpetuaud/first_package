from setuptools import _install_setup_requires, setup

setup(
    name='my_shoes_pkg',
    version='0.0.1',
    packages=['my_shoes_pkg'],
    scripts=["scripts/buy_shoes"],
)