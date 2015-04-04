# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428033809.167025
_enable_loop = True
_template_filename = '/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/event_catalog.detail.html'
_template_uri = 'event_catalog.detail.html'
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
        venue = context.get('venue', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        event = context.get('event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        saleitem_list = context.get('saleitem_list', UNDEFINED)
        address = context.get('address', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        venue = context.get('venue', UNDEFINED)
        def content():
            return render_content(context)
        event = context.get('event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        saleitem_list = context.get('saleitem_list', UNDEFINED)
        address = context.get('address', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="container col-md-9">\n\n\t<h2>')
        __M_writer(str(event.name))
        __M_writer('</h2>\n\n\t<hr>\n      <div id="singleProduct" class="">\n        <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/civil_war.jpg">\n        <div id=\'desc\'>\n        <h3>General Info</h3>\n        <div id=\'list\'>Start Date: ')
        __M_writer(str(event.startDate.strftime('%m/%d/%Y')))
        __M_writer("</div>\n        <div id='list'>End Date: ")
        __M_writer(str(event.endDate.strftime('%m/%d/%Y')))
        __M_writer("</div>\n        <div id='list'>Venue: ")
        __M_writer(str(venue.name))
        __M_writer("</div>\n        <hr>\n        <h3>Address Info</h3>\n        <div id='list'>")
        __M_writer(str(address.street1))
        __M_writer("</div>\n        <div id='list'>")
        __M_writer(str(address.city))
        __M_writer("</div>\n        <div id='list'>")
        __M_writer(str(address.state))
        __M_writer("</div>\n        <div id='list'>")
        __M_writer(str(address.country))
        __M_writer("</div>\n        <div id='list'>")
        __M_writer(str(address.ZIP))
        __M_writer('</div>\n        \n')
        if areas:
            __M_writer('        <hr>\n          <h3>Available Areas</h3>\n')
            for area in areas:
                __M_writer('            <h4>')
                __M_writer(str(area.name))
                __M_writer("</h4>\n            <div id='list'>Description: ")
                __M_writer(str(area.description))
                __M_writer("</div>\n            <div id='list'>Area Number: ")
                __M_writer(str(area.placeNumber))
                __M_writer('</div>\n')
        __M_writer('        \n')
        if saleitem_list:
            __M_writer('        <hr>\n          <h3>Sale Items</h3>\n')
            for s in saleitem_list:
                __M_writer('            <h4>')
                __M_writer(str(s.name))
                __M_writer("</h4>\n            <div id='list'>Description: ")
                __M_writer(str(s.description))
                __M_writer("</div>\n            <div id='list'>Low Price: ")
                __M_writer(str(s.lowPrice))
                __M_writer("</div>\n            <div id='list'>High Price: ")
                __M_writer(str(s.highPrice))
                __M_writer('</div>\n')
        __M_writer('\n          \n\t        \n        </div>\n      </div>\n      \n\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/event_catalog.detail.html", "line_map": {"27": 0, "40": 1, "50": 3, "62": 3, "63": 6, "64": 6, "65": 10, "66": 10, "67": 13, "68": 13, "69": 14, "70": 14, "71": 15, "72": 15, "73": 18, "74": 18, "75": 19, "76": 19, "77": 20, "78": 20, "79": 21, "80": 21, "81": 22, "82": 22, "83": 24, "84": 25, "85": 27, "86": 28, "87": 28, "88": 28, "89": 29, "90": 29, "91": 30, "92": 30, "93": 33, "94": 34, "95": 35, "96": 37, "97": 38, "98": 38, "99": 38, "100": 39, "101": 39, "102": 40, "103": 40, "104": 41, "105": 41, "106": 44, "112": 106}, "source_encoding": "ascii", "uri": "event_catalog.detail.html"}
__M_END_METADATA
"""
