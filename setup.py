from setuptools import setup

VERSION = '0.10.2'

setup(
    name='react-render-client',
    version=VERSION,
    packages=['react_render'],
    install_requires=[
        'django>=1.6',
        'requests>=2',
    ],
    description='Render and bundle React components from a Django application',
    long_description='Documentation at https://github.com/mic159/react-render',
    author='Michael Cooper',
    author_email='mic159@gmail.com',
    url='https://github.com/mic159/react-render',
)
