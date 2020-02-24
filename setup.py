from setuptools import find_packages, setup

setup(
    name='files-collector',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-httpauth'
    ],
    description = 'A simple web-based tool for collecting supplementary files for presentations and speeches for the project ELITR (elitr.eu).'
)
