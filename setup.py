""" Setup configuration for servertools """
from setuptools import find_packages, setup

setup(
    name="servertools",
    version="0.0.2",
    description="Various tools for managing or checking servers",
    author="sWallyx",
    keywords=["python", "scripts", "server", "tools", "dns", "records"],
    classifiers=[],
    install_requires=["dnspython"],
    setup_requires=[],
    tests_require=[],
    packages=find_packages(),
)
