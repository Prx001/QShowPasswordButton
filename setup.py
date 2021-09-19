import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "QShowPasswordButton\\README.md").read_text()
setup(
	name="QShowPasswordButton",
	version="1.0.0",
	description="A customized button to change the visibility of password characters for Qt Python binding PyQt (PyQt5)",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/Prx001/QShowPasswordButton",
	author="Parsa.py",
	author_email="munichbayern2005@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: Implementation :: CPython"
	],
	packages=["QSwitchControl"],
	include_package_data=True,
	install_requires=["PyQt5"]
)
