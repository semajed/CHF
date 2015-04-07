# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428447158.466415
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
        areas = context.get('areas', UNDEFINED)
        saleitem_list = context.get('saleitem_list', UNDEFINED)
        event = context.get('event', UNDEFINED)
        venue = context.get('venue', UNDEFINED)
        address = context.get('address', UNDEFINED)
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
        areas = context.get('areas', UNDEFINED)
        saleitem_list = context.get('saleitem_list', UNDEFINED)
        event = context.get('event', UNDEFINED)
        venue = context.get('venue', UNDEFINED)
        address = context.get('address', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="container col-md-9">\n\n\t<h2>')
        __M_writer(str(event.name))
        __M_writer('</h2>\n\n\t<hr>\n      <div id="singleProduct" class="">\n        <img src="')
        __M_writer(str(event.photo.image))
        __M_writer('">  \n        <div id=\'desc\'>\n        <h3>General Info</h3>\n        <div id=\'list\'>Start Date: ')
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
{"source_encoding": "ascii", "uri": "event_catalog.detail.html", "line_map": {"27": 0, "39": 1, "49": 3, "60": 3, "61": 6, "62": 6, "63": 10, "64": 10, "65": 13, "66": 13, "67": 14, "68": 14, "69": 15, "70": 15, "71": 18, "72": 18, "73": 19, "74": 19, "75": 20, "76": 20, "77": 21, "78": 21, "79": 22, "80": 22, "81": 24, "82": 25, "83": 27, "84": 28, "85": 28, "86": 28, "87": 29, "88": 29, "89": 30, "90": 30, "91": 33, "92": 34, "93": 35, "94": 37, "95": 38, "96": 38, "97": 38, "98": 39, "99": 39, "100": 40, "101": 40, "102": 41, "103": 41, "104": 44, "110": 104}, "filename": "/Users/jamesdayhuff/Documents/Programming/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/event_catalog.detail.html"}
__M_END_METADATA
"""
