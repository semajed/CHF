# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425760913.440348
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/catalog.detail.html'
_template_uri = 'catalog.detail.html'
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
        qty = context.get('qty', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
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
        qty = context.get('qty', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container col-md-9">\n\n\t<h3>Product Details\n\t\t<button class="view_button btn btn-md btn-info pull-right">View Cart<span id="cart" class="glyphicon glyphicon-shopping-cart"></span></button>\n\t</h3>\n\n\t<hr>\n      <div id="singleProduct" class="text-muted">\n        <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/CannonFinished.jpg">\n        <div id=\'desc\'>\n\t        <div id=\'list\'>Name: ')
        __M_writer(str(product.name))
        __M_writer("</div>\n\t        <div id='list'>Description: ")
        __M_writer(str(product.description))
        __M_writer("</div>\n\t        <div id='list'>Price: $")
        __M_writer(str(product.currentPrice))
        __M_writer('</div>\n\t        <br>\n\t        <button id=\'deetPic\' data-pid="')
        __M_writer(str( product.id ))
        __M_writer('" data-qty="')
        __M_writer(str(qty))
        __M_writer('" class="add_button btn btn-warning">Add to cart</button>\n        </div>\n      </div>\n      \n\n    </div>\n\n\n<div id="shopping_cart_modal" class="modal fade">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Shopping Cart</h4>\n      </div>\n      <div class="shopping_cart_contents">\n      </div>\n      <div class="modal-footer">\n')
        __M_writer('      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "catalog.detail.html", "source_encoding": "ascii", "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/catalog.detail.html", "line_map": {"64": 16, "65": 18, "66": 18, "27": 0, "68": 18, "37": 1, "75": 69, "47": 3, "67": 18, "69": 37, "56": 3, "57": 12, "58": 12, "59": 14, "60": 14, "61": 15, "62": 15, "63": 16}}
__M_END_METADATA
"""
