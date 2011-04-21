from setuptools import setup, find_packages
import os, fnmatch
import profiling

media_files = []

for dirpath, dirnames, filenames in os.walk(os.path.join('profiling', 'media')):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        failed = False
        for pattern in ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*'):
            if fnmatch.fnmatchcase(filename, pattern):
                failed = True
        if failed:
            continue
        media_files.append(os.path.join(*filepath.split(os.sep)[1:]))
        
if profiling.VERSION[-1] == 'final':
    CLASSIFIERS = ['Development Status :: 5 - Production/Stable']
elif 'beta' in profiling.VERSION[-1]:
    CLASSIFIERS = ['Development Status :: 4 - Beta']
else:
    CLASSIFIERS = ['Development Status :: 3 - Alpha']

CLASSIFIERS += [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Frank Bieniek",
    author_email="seo_link@produktlaunch.de",
    name='django-profiling',
    version=profiling.__version__,
    description='An Profiling Middleware',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='http://github.com/FrankBie/django-profiling/',
    download_url='http://github.com/FrankBie/django-profiling/downloads',
    license='MIT License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
    ],
    packages=find_packages(exclude=["example", "example.*","testdata","testdata.*"]),
    package_data={
        'profiling': [
            
        ]
    },
    test_suite = "",
    zip_safe = False
)
