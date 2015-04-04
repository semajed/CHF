# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428028127.463519
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/event_catalog.html'
_template_uri = 'event_catalog.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<title>Catalog</title>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Event Catalog</h1>\n    \n    \n    <hr>\n    <div class="row">\n      <div class="col-lg-4">\n        <div class="input-group">\n          <input type="text" id="searchBar" class="form-control" placeholder="Search for...">\n          <span class="input-group-btn">\n            <button class="btn btn-default" type="button">Go!</button>\n          </span>\n        </div><!-- /input-group -->\n      </div><!-- /.col-lg-6 -->\n\n    </div><!-- /.row -->\n    <hr>\n    <div id="productList" class="container col-md-12">\n')
        for event in events:
            __M_writer('            <div class="box text-muted">\n              <h5 id="pname">')
            __M_writer(str(event.name))
            __M_writer('</h5>\n              <hr>\n              <a href=\'\'>\n                <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/civil_war.jpg">  \n              </a>  \n              <h5>Start Date: ')
            __M_writer(str(event.startDate.strftime('%m/%d/%Y')))
            __M_writer('</h5>\n              <h5>End Date: ')
            __M_writer(str(event.endDate.strftime('%m/%d/%Y')))
            __M_writer('</h5>\n              <a role=\'button\' href="/homepage/event_catalog.detail/')
            __M_writer(str(event.id))
            __M_writer('/" class="add_button btn btn-info">View Details</a>\n            </div>\n\n')
        __M_writer('    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 29, "65": 30, "66": 30, "27": 0, "36": 1, "73": 67, "46": 3, "67": 34, "54": 3, "55": 21, "56": 22, "57": 23, "58": 23, "59": 26, "60": 26, "61": 28, "62": 28, "63": 29}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/event_catalog.html", "source_encoding": "ascii", "uri": "event_catalog.html"}
__M_END_METADATA
"""
