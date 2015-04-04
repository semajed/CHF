# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428033493.030009
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/catalog.html'
_template_uri = 'catalog.html'
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
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<title>Catalog</title>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <h1>Product Catalog</h1>\n    \n    \n    <hr>\n    <div class="row">\n      <div class="col-lg-4">\n        <div class="input-group">\n          <input type="text" id="searchBar" class="form-control" placeholder="Search for...">\n          <span class="input-group-btn">\n            <button class="btn btn-default" type="button">Go!</button>\n          </span>\n        </div><!-- /input-group -->\n      </div><!-- /.col-lg-6 -->\n      <button class="view_button btn btn-md btn-info pull-right">View Cart<span id="cart" class="glyphicon glyphicon-shopping-cart"></span></button>\n    </div><!-- /.row -->\n    <hr>\n    <div id="productList" class="container col-md-12">\n')
        for product in products:
            __M_writer('            <div class="box text-muted">\n              <h5 id="pname">')
            __M_writer(str(product.name))
            __M_writer("</h5>\n              <hr>\n              <a href='/homepage/catalog.detail/")
            __M_writer(str(product.id))
            __M_writer('/1\'>\n                <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/CannonFinished.jpg">  \n              </a>            \n              <h5>$')
            __M_writer(str(product.currentPrice))
            __M_writer('</h5>\n')
            __M_writer('              <button data-pid="')
            __M_writer(str( product.id ))
            __M_writer('" class="add_button btn btn-xs btn-warning">Add to cart</button>\n            </div>\n')
        __M_writer('    </div>\n\n\n<div id="shopping_cart_modal" class="modal fade">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Shopping Cart</h4>\n      </div>\n      <div class="shopping_cart_contents">\n      \n      </div>\n      <div class="modal-footer">\n')
        __M_writer('      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/catalog.html", "source_encoding": "ascii", "uri": "catalog.html", "line_map": {"64": 28, "65": 28, "66": 30, "27": 0, "36": 1, "69": 33, "68": 30, "41": 52, "76": 70, "70": 48, "47": 3, "67": 30, "55": 3, "56": 21, "57": 22, "58": 23, "59": 23, "60": 25, "61": 25, "62": 26, "63": 26}}
__M_END_METADATA
"""
