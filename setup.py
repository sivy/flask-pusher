"""
Flask-Pusher
-------------

Pusher support for Flask.

http://pusherapp.com/

"""
from setuptools import setup


setup(
    name='Flask-Pusher',
    version='0.1',
    url='',
    license='BSD',
    author='Steve Ivy',
    author_email='steveivy@wallrazer.com',
    description='Pusher support for Flask',
    long_description=__doc__,
    py_modules=['flask.ext.pusher'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
