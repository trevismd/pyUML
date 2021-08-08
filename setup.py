from setuptools import setup

setup(
    name='pyUML',
    version='0.0.1',
    package_dirs={
        'pyUML': 'pyUML'
    },
    install_requires=["pydot", "graphviz"],
    packages=['pyUML'],
    url='',
    license='GNU GPLv3',
    author='Florian Charlier',
    author_email='florian.charlier@cascliniques.be',
    description='Create simple Graphviz dot UML graphs with a python script'
)
