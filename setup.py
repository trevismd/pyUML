from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pyUML',
    version='0.1.0a',
    package_dirs={
        'pyUML': 'pyUML'
    },
    install_requires=["pydot"],
    packages=['pyUML'],
    url='https://githib.com/trevismd/pyUML',
    license='GNU GPLv3',
    author='Florian Charlier',
    author_email='florian.charlier@cascliniques.be',
    description='Create simple GraphViz DOT UML graphs with a python script',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
)
