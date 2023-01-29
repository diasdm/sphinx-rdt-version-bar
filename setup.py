import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sphinx_rdt_version_bar",
    version="0.0.0",
    author="David Dias",
    author_email="david6dias@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=["sphinx", "sphinx-rtd-theme"],
)
