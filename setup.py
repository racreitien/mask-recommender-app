from setuptools import setup

setup(
    name='Should I Wear a Mask',
    version='1.0',
    long_description=__doc__,
    packages=['shouldiwearamask'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'redirect', 'render_template', 'request']
)