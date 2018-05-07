import re
from os import path
from codecs import open  # To use a consistent encoding
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Get version without importing, which avoids dependency issues
def get_version():
    with open('voting_smartcontract/__init__.py') as version_file:
        return re.search(r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""",
                         version_file.read()).group('version')


install_requires = ['neo-python']


test_requires = ['pytest', 'pytest-sugar', 'pytest-asyncio', 'pytest-cov', ]


setup(
    name='voting-smartcontract',
    description="Project to deploy a smart contract for voting app.",
    long_description=long_description,
    version=get_version(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=test_requires,
    packages=find_packages(),
    zip_safe=False,
    author="Ankur Srivastava",
    author_email="ankur.srivastava@email.de",
    download_url="github.com/ansrivas/{}.tar.gz".format(get_version()),
    classifiers=[
        "Programming Language :: Python :: 3.6"]
)
