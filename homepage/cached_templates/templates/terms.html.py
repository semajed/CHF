# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421190399.534579
_enable_loop = True
_template_filename = '/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer('\n    <h1>This is the terms view content</h1>\n    <div class="panel panel-default col-md-10">\n\t  <div class="panel-heading">\n\t    <h3 class="panel-title">Terms & Conditions</h3><span class="label label-danger">Important</span>\n\t  </div>\n\t  <div class="panel-body">\n\t    <p>Bacon ipsum dolor amet picanha ground round porchetta leberkas, shankle shank swine ribeye boudin sirloin pancetta sausage andouille strip steak. Doner frankfurter chuck shoulder salami biltong. Pancetta cow brisket, landjaeger doner turducken jowl shankle pork ground round filet mignon. Porchetta rump pastrami brisket corned beef beef ribs tail sirloin, spare ribs tongue landjaeger leberkas ribeye capicola hamburger.\n\t    </p>\n\n\t\t<p>Cupim biltong chuck shoulder meatloaf jowl short loin venison prosciutto. Ribeye tail spare ribs ground round sausage. Picanha turducken meatball, jerky boudin corned beef sirloin. Sirloin salami swine spare ribs bacon ribeye corned beef meatloaf kielbasa.\n\t\t</p>\n\n\t\t<p>Pig venison swine pork loin ball tip alcatra kielbasa landjaeger chicken spare ribs meatball meatloaf andouille. Short loin salami ham hock tail turducken venison pig tongue meatball cupim drumstick shoulder. Turkey ground round brisket ham. Tail leberkas beef capicola pork belly kielbasa pig shankle. Tenderloin sausage porchetta swine ball tip fatback filet mignon prosciutto shoulder meatball pig kielbasa ground round pork loin. Ground round spare ribs tenderloin shank turkey prosciutto. Cow chuck prosciutto chicken leberkas landjaeger.\n\t\t</p>\n\n\t\t<p>Salami pork belly corned beef beef ribs jerky, shankle picanha tail ham hock pork. Short ribs bacon bresaola salami filet mignon cupim. Sausage swine chicken spare ribs, alcatra sirloin ham flank. Pancetta biltong swine beef ribs chuck cow pastrami rump brisket frankfurter. Frankfurter venison filet mignon, pork loin tenderloin chuck fatback spare ribs biltong turducken tongue.\n\t\t</p>\n\n\t\t<p>T-bone sausage picanha, jerky venison landjaeger ball tip capicola cow cupim. Leberkas pork chop boudin, ribeye kevin tri-tip short loin beef ribs pancetta. Salami jerky corned beef prosciutto ball tip andouille. Ground round tenderloin bacon biltong. Biltong tongue pork loin hamburger strip steak flank, cupim short loin.\n\t\t</p>\n\t\t<button type="button" class="btn btn-success pull-right">I Agree</button>\n\t  </div>\n\t</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "terms.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "filename": "/Library/Frameworks/Python.framework/Versions/3.4/bin/test_dmp1/homepage/templates/terms.html"}
__M_END_METADATA
"""
