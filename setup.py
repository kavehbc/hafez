import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', "r") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    package_data={'': ['data/*.db']},
)
