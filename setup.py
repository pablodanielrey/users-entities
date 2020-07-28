from setuptools import setup, find_packages, find_namespace_packages

setup(name="user-entities",
    version="0.0.1",
    package_dir={"":"src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        'SQLAlchemy'
    ]
)