from setuptools import setup

classifiers = [
    #'Development Status :: 5 - Production/Stable',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
]

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'oecx',
  packages = ['oecx'], # this must be the same as the name above
  version = '0.1.0',
  description = 'Network builder for the Observatory for Economic Complexity ',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Francisco R. Lanza',
  author_email = 'frjrodriguezla@unal.edu.co',
  license='MIT',
  url = 'https://github.com/frjrodriguezla/oecx', # use the URL to the github repo
  keywords = ['oec', 'network'],
  classifiers = classifiers,
  install_requires=['requests','networkx'],
  python_requires='>=3',
  py_modules=['oecx']
)
