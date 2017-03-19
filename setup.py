from setuptools import setup


setup(
    name='PyLexTo',
    version='0.1.2',
    description='LongLexTo with Python wrapper',
    url='https://github.com/catmium/PyLexTo',
    author='catmium',
    packages=['PyLexTo'],
    install_requires=['JPype1==0.6.2'],
    license='GPL-3.0',
    author_email='hello@jets.im',
    package_data={'': ['LICENSE'],
                  'PyLexTo': ['LongLexTo', 'data/dictionary/*.txt', 'data/stopwords/*.txt']}
)