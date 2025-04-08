""" Setup configuration for CTRL_Node """
from setuptools import find_packages, setup

setup(
    name="CTRL_Node",
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
