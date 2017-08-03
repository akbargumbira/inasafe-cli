# coding=utf-8
"""Setup file for distutils / pypi."""
try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages


setup(
    name='inasafe_cli',
    version='4.2.0',
    packages=find_packages(),
    license='GPL',
    author='InaSAFE Team',
    author_email='info@inasafe.org',
    url='http://inasafe.org/',
    description=('Realistic natural hazard impact scenarios for better '
                 'planning, preparedness and response activities.'),
    install_requires=[
        # 'inasafe',
        'docopt'
    ],
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPL V3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
