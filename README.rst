Profiling APP
-------------
Your Django became too slow?

Install
========
add this to your settings.py

	INSTALLED_APPS += ['profiling']
	MIDDLEWARE_CLASSES += ['profiling.middleware.InstrumentMiddleware']

	pip install pyprof2calltree for cachgrinder

How to do a profiling run
--------------------------
	add a get param: "cprofile" to start profiling

	add a get param: "profile-stop" to stop profiling
 
	the log will be in the tmp/profiler folder of your system


Inspired by
----------- 
	http://lurkingideas.net/profiling-django-projects-cachegrind/


CacheGrinder
------------
	pyprof2calltree -i logfilename.pro -k

	or

	pyprof2calltree -i logfilename.pro -o callgrinder.logfilename.log


additional Profiling Resources:
-------------------------------
	TBD


