#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-process-street",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_process_street"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python==5.9.1",
        "requests==2.24.0",
    ],
    entry_points="""
    [console_scripts]
    tap-process-street=tap_process_street:main
    """,
    packages=["tap_process_street"],
    package_data = {
        "schemas": ["tap_process_street/schemas/*.json"]
    },
    include_package_data=True,
)
