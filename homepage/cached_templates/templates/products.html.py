# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423004725.579659
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/products.html'
_template_uri = 'products.html'
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
        products = context.get('products', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <h1>This is the product management page</h1>\n    <p><a class="btn btn-primary btn-lg" href="/homepage/products.create" role="button">Create Product</a></p>\n\n    <div class="container col-md-9">\n      <table id="roleTable" class="table table-hover">\n        <tr >\n          <th>Name</th>\n          <th>Description</th>\n          <th>Category</th>\n          <th>Current Price</th>\n          <th>Person</th>\n          <th>Action</th>\n        </tr>\n')
        for product in products:
            __M_writer('        <tr>\n          <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n          <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n          <td>')
            __M_writer(str(product.category))
            __M_writer('</td>\n          <td>')
            __M_writer(str(product.currentPrice))
            __M_writer('</td>\n          <td>')
            __M_writer(str(product.person.name))
            __M_writer('</td>\n          <td>\n          <a class=\'btn btn-xl btn-primary\' href="/homepage/products.edit/')
            __M_writer(str(product.id))
            __M_writer('/">EDIT</a>\n          </td>\n        </tr>\n')
        __M_writer('      </table>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 23, "65": 25, "66": 25, "35": 1, "73": 67, "45": 3, "27": 0, "67": 29, "52": 3, "53": 17, "54": 18, "55": 19, "56": 19, "57": 20, "58": 20, "59": 21, "60": 21, "61": 22, "62": 22, "63": 23}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/products.html", "uri": "products.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
