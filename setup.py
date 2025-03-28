from setuptools import setup

# Read version without importing
version = {}
with open(os.path.join('postmark', '__init__.py')) as f:
    exec(f.read(), version)

setup(
    name="python-postmark",
    version=__version__,  # Use static version
    packages=['postmark'],
    author="Dave Martorana (http://davemartorana.com), Richard Cooper (http://frozenskys.com), Bill Jones (oraclebill), Dmitry Golomidov (deeGraYve)",
    author_email="themartorana@gmail.com",
    license='BSD',
    description="Postmark library for Python 2.7 and greater.",
    long_description="Note: To use Python 2.4 or 2.5, please use python-postmark version 0.3.2. Python 2.6 use version 0.4.4.",
    url="http://github.com/themartorana/python-postmark",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
    ]
)