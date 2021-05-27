from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'RanPassCLI',
    version = '0.0.1',
    author = 'Damian Sanchez',
    author_email = 'damiansanchez@onmail.com',
    license = 'MIT',
    description = 'Random password generator',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/Damian-Sanchez/ranpasscli',
    py_modules = ['ranpasscli', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #Command 'ranpasscli' will trigger main() in ranpasscli.py
    entry_points = '''
        [console_scripts]
        ranpasscli=ranpasscli:main
    '''
)