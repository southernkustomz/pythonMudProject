from setuptools import setup, find_packages

setup(
    name='pythonMudProject',
    extras_required=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"},
)