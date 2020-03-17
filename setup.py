from setuptools import setup

setup(
   name='eric-pdf',
   version='1.0',
   description='Module to extract product data from site PDFs',
   author='Bart Timmer',
   author_email='bchtimmer@gmail.com',
   packages=['eric-pdf'],  #same as name
   install_requires=['PyPDF2', 'pandas', 'tabula', 'tabula-py', 'xlsxwriter'], #external packages as dependencies
)
