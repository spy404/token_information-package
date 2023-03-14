from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='token_information',
  version='1.0.0',
  description='token_information is a Python Package created for scraping discord account data with the use of an account token.',
  long_description=open('README.md').read(),
  url='https://github.com/spy404/token_information-package',  
  author='spy404',
  author_email='spy404.work@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['discord', 'token', 'token_info', 'spy404'], 
  packages=find_packages(),
  install_requires=['requests', 'pystyle'] 
)
