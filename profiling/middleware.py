# -*- coding: utf-8 -*-
import cProfile
from datetime import datetime
import os, errno
import logging as log
import tempfile

tempdir = tempfile.gettempdir()

class InstrumentMiddleware(object):
    
    def process_request(self, request):
        #ignore media
        if self._is_path_ignoreable(request, ['/media', '/static']):
            return
        # activate profiling?
        if 'cprofile' in request.GET:
            log.debug("activate profiling")
            request.session['cprofile'] = True
        # stop profiling
        if 'cprofile-stop' in request.GET and request.session.get('cprofile'):
            log.debug("deactivate profiling")
            request.session['cprofile'] = False
            
        if hasattr(request, 'session') and request.session.get('cprofile'): 
            if not hasattr(request, 'profiler'):
                log.debug("start profiling")
                request.profiler = cProfile.Profile()
            log.debug("enable profiling")
            request.profiler.enable()

    def process_response(self, request, response):
        # operate only on text/html
        if 'text/html' not in response['Content-Type']:
            if hasattr(request, 'profiler'):
                log.debug("disable profiler")
                request.profiler.disable()
            return response
        
        # are we in a profiler run
        if request.session.get('cprofile') and hasattr(request, 'profiler'): 
            request.profiler.disable()
            # store the output
            tmpfolder = tempfile.tempdir
            tmpfolder = "%s%s%s" % (tmpfolder, os.sep, "profiler")
            try:
                os.makedirs(os.path.normpath(tmpfolder))
            except OSError, e:
                if e.errno != errno.EEXIST:
                    raise
            log_filename = ("%s-%s.pro" % (request.META['REMOTE_ADDR'], datetime.now())).replace(" ", "_").replace(":", "-")
            location = "%s%s%s" % (tmpfolder, os.sep, log_filename)
            request.profiler.dump_stats(location)
            log.debug("wrote profiling log: %s" % (location))
            log.debug("for request path: %s" % (request.META["PATH_INFO"]))
        
        # stop the profiler run
        if request.session.get('cprofile') == False and hasattr(request, 'profiler'): 
            try:
                del request.session['cprofile']
                del request.profiler
                log.debug("removed profiling from session")
            except KeyError:
                pass

        return response
    
    def _is_path_ignoreable(self, request, ignore_pathes):
    #@TODO: get the media path from the settings
        ignoreable = False
        for ignore_path in ignore_pathes:
            if unicode(request.META['PATH_INFO']).find(ignore_path) == 0:
                ignoreable = True
                break
        return ignoreable  

