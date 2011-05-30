from distutils.core import setup
import mcauth

long_description = open('README.rst').read()

setup(
    name='mcauth',
    version='%d.%d' % (mcauth.VERSION[0], mcauth.VERSION[1]),
    description='Django backend for Minecraft.net authentication.',
    long_description=long_description,
    author='Gregory Taylor',
    author_email='gtaylor@gc-taylor.com',
    license='BSD License',
    url='https://github.com/gtaylor/django-mcauth/',
    platforms=["any"],
    provides=['mcauth'],
    packages=[
        'mcauth',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
