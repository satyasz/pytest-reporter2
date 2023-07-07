from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pytest-reporter2',
    version='0.0.3',
    author='Satya S',
    author_email='satyasz100@gmail.com',
    maintainer='Satya S',
    maintainer_email='satyasz100@gmail.com',
    license='MIT',
    license_file='LICENSE',
    url='https://github.com/satyasz/pytest-reporter2',
    description='Generate Pytest reports with templates (modified)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pytest_reporter2'],
    python_requires='>=3.5',
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'reporter = pytest_reporter2.plugin',
        ],
    },
)
