# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421187846.190693
_enable_loop = True
_template_filename = '/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        __M_writer = context.writer()
        __M_writer('\n    <h1>This is the contact view content</h1>\n    <div class="page-header">\n  \t\t<h1>Contact Us! <small>Anytime.</small></h1>\n\t</div>\n\t<div clas="panel panel-default">\n\t\t<div class="container">\n\t\t\t<form role="form" class="col-md-10">\n\t\t\t\t<div class="form-group">\n\t\t    \t\t<label for="InputEmail">Your Email Address</label>\n\t\t   \t\t\t<input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter email">\n\t\t \t\t</div>\n\n\t\t \t\t<div class="form-group">\n\t\t    \t\t<label for="studentName">Your Name</label>\n\t\t   \t\t\t<input type="email" class="form-control" id="studentName" placeholder="Enter student name">\n\t\t \t\t</div>\n\n\t\t\t\t<label for="message">Your Message</label>\n\t\t \t\t<textarea class="form-control" rows="5" id="message" placeholder="Please let us know how to help you!"></textarea>\n\t\t \t\t<br>\n\t\t \t\t<button type="button" class="btn btn-primary pull-right">Send <span class="glyphicon glyphicon-send"></span></button>\n\t\t\t</form>\n\t\t\t\n\t\t\t\n\t\t</div>\n\t\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "contact.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "filename": "/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/contact.html"}
__M_END_METADATA
"""
