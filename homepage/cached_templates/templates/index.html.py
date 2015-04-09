# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428553229.334478
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html'
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if request.user.username != '':
            __M_writer('\t\t<div id="personalHello">\n\t\t\t<h1 >Hello, ')
            __M_writer(str(request.user.get_full_name()))
            __M_writer('!</h1>\n\t\t</div>\n')
        else:
            __M_writer('\t\t<div id="personalHello">\n\t\t\t<h1>Hello, Visitor!</h1>\n\t\t</div>\n')
        __M_writer('\t<hr>\n    <div class="jumbotron">\n')
        __M_writer('        <h1>Colonial Heritage Foundation</h1>\n        <p>\n            Welcome to the Colonial Heritage Foundation website! This foundation provides\n            opportunities to you to experience the colonial life through various events and products\n            available for you to purchase or rent.\n        </p>\n        <p><a class="btn btn-primary btn-lg pull-right" href="/homepage/users.userCreate" role="button">Create Account</a></p>\n\n')
        __M_writer('    </div>\n    <br>\n      <hr>\n      <br>\n          <div class="snapshots">\n\n      <div class="col-lg-4">\n      <img class="img-circle thing_blurb" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Events/colonial_event.jpg">\n          <h2>Attend Events!</h2>\n          <p>These events are put on by a fantastic group of volunteers that help you experience life in the colonial times!\n          Click to see more details...</p>\n\n          <p><a class="btn btn-primary" href="/homepage/event_catalog" role="button">View details &raquo;</a></p>\n       </div>\n\n       <div class="col-lg-4">\n       <img class="img-circle thing_blurb" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Products/products_purhcase.jpg">\n          <h2>Buy Colonial Products!</h2>\n          <p>Interested in buying colonial era products? Come checkout the product catalog!</p>\n          <p><a class="btn btn-primary" href="/homepage/catalog" role="button">View details &raquo;</a></p>\n       </div>\n\n       <div class="col-lg-4">\n       <img class="img-circle thing_blurb" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/Items/rental_thing.jpg">\n          <h2>Rent Colonial Items!</h2>\n          <p>Feel free to rent items we own! Allow us to help you recreate your own experiences!</p>\n          <p><a class="btn btn-primary" href="/homepage/rental_catalog" role="button">View details &raquo;</a></p>\n       </div>\n       </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/index.html", "uri": "index.html", "line_map": {"64": 26, "65": 33, "66": 33, "27": 0, "36": 1, "69": 49, "68": 42, "41": 55, "76": 70, "70": 49, "47": 4, "67": 42, "55": 4, "56": 5, "57": 6, "58": 7, "59": 7, "60": 9, "61": 10, "62": 14, "63": 17}, "source_encoding": "ascii"}
__M_END_METADATA
"""
