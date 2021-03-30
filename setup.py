import setuptools

VERSION = '0.2.1'

setuptools.setup(
    name='mts_logging',
    version=VERSION,
    description='Another Python logger',
    url='https://github.com/mts7/mts-logger',
    author='Mike Rodarte',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['*_test.', 'test_*.']),
    classifiers=[
        'License:: OSI Approved:: MIT License',
        'Operating System:: OS Independent',
        'Programming Language:: Python:: 3',
        'Programming Language:: Python:: 3.8',
        'Programming Language:: Python:: 3.9',
    ],
    python_requires='>=3.8',
    install_requires=[
        'colorama'
    ],
)
