Profiling APP
-------------

Install
========
pip install pyprof2calltree

MIDDLEWARE_CLASSES = (
    ...
    'project.apps.myapp.middleware.InstrumentMiddleware',
    ...


Inspired by
----------- 
http://lurkingideas.net/profiling-django-projects-cachegrind/



Execution
---------
add a get param: cprofile to start profiling
add a get param: profile-stop to stop profiling
 
the log will be in the tmp/profiler folder of your system

CacheGrinder
------------
pyprof2calltree -i logfilename.pro -k
or
pyprof2calltree -i logfilename.pro -o callgrinder.logfilename.log

