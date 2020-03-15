from setuptools import setup, find_packages
import httpservice

setup(
    name='HttpService',
    author='Adebayo John Oluwasegun',
    author_email='john.bayo@web.de',
    packages=find_packages(),
    version=httpservice.__version__,
    license='MIT',
    description='Packaged HTTPS Service',
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 3.x",
    ],
    entry_points={
        'console_scripts': [
            'myhttpservice = httpservice.app:main'
        ]
    }
)
