# coding: utf-8
from setuptools import setup


with open('README.md') as readme_file:
   long_description = readme_file.read()


setup(
   name="typeracer_cheat",
   version="0.0.2",
   author="RoastSea8 (Aditya Tomar)",
   author_email="aditya26042005@gmail.com",
   description="A program that allows one to achieve extremely high speeds on typeracer.com on all game modes.",
   license="MIT",
   keywords=['typeracer', 'cheat', 'typeracercheat', 'typecheat', 'typefast', 'chromedriver', 'selenium', 'onlineraces'],
   url="https://github.com/RoastSea8/typeracer-cheat",
   packages=["typeracer_cheat"],
   entry_points = {
        'console_scripts': ['type_cheat=typeracer_cheat.command_line:type_cheat'],
   },
   install_requires=['selenium', 'chromedriver_autoinstall'],
   long_description_content_type="text/markdown",
   long_description=long_description,
   python_requires=">=3.6",
   classifiers=[
      "Development Status :: 4 - Beta",
      "Topic :: Software Development :: Testing",
      "Topic :: System :: Installation/Setup",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: Microsoft :: Windows",
   ],
)