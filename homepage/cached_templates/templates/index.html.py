# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421185314.447544
_enable_loop = True
_template_filename = '/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html'
_template_uri = 'index.html'
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
        __M_writer('\n    <h1>This is the index view content</h1>\n    <div class="jumbotron col-md-9">\n      <div class="container">\n        <h1>Meat, the essence of food.</h1>\n        <p>Meatball turkey bresaola shoulder porchetta tail prosciutto pork chop flank tenderloin short ribs pork belly. Cow bacon ground round doner ham pig turkey strip steak picanha ham hock t-bone. Kevin shankle capicola, andouille swine chicken tongue biltong pork. Pastrami doner rump drumstick swine short ribs.</p>\n        <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more &raquo;</a></p>\n      </div>\n    </div>\n    \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "filename": "/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html"}
__M_END_METADATA
"""
