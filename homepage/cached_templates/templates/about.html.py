# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422563521.693483
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/about.html'
_template_uri = 'about.html'
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
        events = context.get('events', UNDEFINED)
        allEmployees = context.get('allEmployees', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
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
        events = context.get('events', UNDEFINED)
        allEmployees = context.get('allEmployees', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>This is the about view content</h1>\n    \n    <div class="clearFix">\n      <div>\n        <a href="/homepage/about.create/"><button class="btn btn-primary">Create New User</button></a>\n      </div>\n    </div>\n    <br>\n\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-striped">\n        <tr>\n          <th>ID</th>\n          <th>First Name</th>\n          <th>Last Name</th>\n          <th>Position</th>\n          <th>Action</th>\n        </tr>\n')
        for emp in allEmployees:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(emp.id))
            __M_writer('</td>\n          <td>')
            __M_writer(str(emp.firstName))
            __M_writer('</td>\n          <td>')
            __M_writer(str(emp.lastName))
            __M_writer('</td>\n          <td>')
            __M_writer(str(emp.position))
            __M_writer('</td>\n          <td>\n          <a href="/homepage/about.edit/')
            __M_writer(str(emp.id))
            __M_writer('/">EDIT</a>\n          |\n          <a href="/homepage/about.edit">DELETE</a>\n          </td>\n\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-striped">\n        <tr>\n          <th>Start Date</th>\n          <th>End Date</th>\n          <th>mapFileName</th>\n        </tr>\n')
        for event in events:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(event.startDate))
            __M_writer('</td>\n          <td>')
            __M_writer(str(event.endDate))
            __M_writer('</td>\n          <td>')
            __M_writer(str(event.mapFileName))
            __M_writer('</td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n    <div class="row">\n        <div class="col-md-9">\n          <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">\n          <h2>Heading</h2>\n          <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.</p>\n        </div><!-- /.col-md-9 -->\n        <div class="col-md-9">\n          <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">\n          <h2>Heading</h2>\n          <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Cras mattis consectetur purus sit amet fermentum. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh.</p>\n        </div><!-- /.col-md-9 -->\n        <div class="col-md-9">\n          <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">\n          <h2>Heading</h2>\n          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>\n        </div><!-- /.col-md-9 -->\n        <div class="col-md-9">\n          <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">\n          <h2>Heading</h2>\n          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>\n        </div><!-- /.col-md-9 -->\n      </div><!-- /.row -->\n \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/about.html", "line_map": {"64": 27, "65": 29, "66": 29, "67": 36, "68": 45, "69": 46, "70": 47, "71": 47, "72": 48, "73": 48, "74": 49, "75": 49, "76": 52, "82": 76, "27": 0, "36": 1, "46": 3, "54": 3, "55": 22, "56": 23, "57": 24, "58": 24, "59": 25, "60": 25, "61": 26, "62": 26, "63": 27}, "uri": "about.html"}
__M_END_METADATA
"""
