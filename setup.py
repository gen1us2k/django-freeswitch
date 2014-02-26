from setuptools import setup, find_packages

setup(
    name='django-freeswitch',
    version=__import__('freeswitch').__version__,
    description='Models for integration FreeSwitch with Django',
    author='Andrew Minkin',
    author_email='minkin.andrew@gmail.com',
    url='https://github.com/gen1us2k/django-freeswitch.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
