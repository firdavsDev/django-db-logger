import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def local_scheme(version):
    return ""


setup(
    name='django-db-logger',
    version='0.1.13',
    # use_scm_version={"local_scheme": local_scheme} if os.getenv('TestPypi') == 'yes' else False,  # using `setuptools_scm` when publish to test.pypi
    setup_requires=['setuptools_scm'],
    packages=['django_db_logger', 'django_db_logger.migrations'],
    include_package_data=True,
    license='MIT License',
    description='Django logging in database',
    long_description=README,
    url='https://github.com/CiCiUi/django-db-logger',
    author='zhangshine',
    author_email='zhangshine0125@gmail.com',
    install_requires=['django>=1.9', 'six'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
