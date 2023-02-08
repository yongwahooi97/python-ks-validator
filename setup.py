from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Python validator that used to validate data during ETL process.'

# Setting up
setup(
        name="ksvalidator", 
        version=VERSION,
        author="Yong Wah",
        author_email="yongwahooi97@gmail.com",
        description=DESCRIPTION,
        long_description=open("README.md", 'r').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/yongwahooi97/python-ks-validator',
        packages=find_packages(),
        install_requires=[
            'pandas',
            'numpy',
            'datetime',
        ],         
        keywords=['python', 'validator'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)