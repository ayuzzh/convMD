from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Tool for converting MD into HTML'

setup(
        name="convMD",
        version=VERSION,
        author="Ayush K M",
        author_email="kmayushkm@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=["ply"],
	license="GPL-3.0",
	url="https://github.com/ayuzzh/convMD",
	keywords=['python', 'markdown', 'html'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
