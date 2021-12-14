from setuptools import find_packages, setup


setup(
    name="mymplrc",
    version="0.0.1",
    description="matplotlib configuration",
    url="https://github.com/eljost/mymplrc",
    maintainer="Johannes Steinmetzer",
    maintainer_email="johannes.steinmetzer@uni-jena.de",
    license="License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    platforms=["unix"],
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
)
