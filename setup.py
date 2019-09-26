import io
import os

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="encryptor",
    version=os.environ['PACKAGE_VERSION'],
    url="https://rafaeelaudibert/encryptor.py",
    maintainer="Rafa Audibert",
    maintainer_email="rafaeelaudibert@gmail.com",
    description="Little toy project to showcase Flask, Sentry and TravisCI for INF01127 - Software Engineering course at UFRGS",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest"]},
)
