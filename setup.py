#!/usr/bin/env python
from __future__ import absolute_import
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

install_requires = ["sentry>=7.0.0", "requests<3.0.0"]

setup(
    name="sentry-auth-oidc",
    version="2.0.0",
    author="Max Wittig",
    author_email="max.wittig@siemens.com",
    url="https://www.getsentry.com",
    description="OpenID Connect authentication provider for Sentry",
    long_description=readme,
    license="Apache 2.0",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={"sentry.apps": ["sentry_auth_oidc = sentry_auth_oidc"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
