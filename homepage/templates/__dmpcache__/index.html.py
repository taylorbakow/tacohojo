# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554783649.9038641
_enable_loop = True
_template_filename = 'C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
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
        self = context.get('self', UNDEFINED)
        sList = context.get('sList', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        formD = context.get('formD', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        sList = context.get('sList', UNDEFINED)
        objectType = context.get('objectType', UNDEFINED)
        formP = context.get('formP', UNDEFINED)
        formD = context.get('formD', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <p>CONTENT GOES HERE</p>\r\n        <div class="grid">\r\n            <form method="post">\r\n                <div class="row">\r\n                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formP ))
        __M_writer(' </div>\r\n                    <div class="col" style="margin-top: 35px;"> <input type="submit" name="Prescriber" value="Search"></div>\r\n                </div>\r\n            </form>\r\n            <form method="post">\r\n                <div class="row">\r\n                    <div class="col"> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( formD ))
        __M_writer(' </div>\r\n                    <div class="col" style="margin-top: 35px;"> <input type="submit" name="Drug" value="Search"></div>\r\n                </div>\r\n            </form>\r\n            <div class="row">\r\n')
        if objectType == 'Prescriber':
            __M_writer('                    <ul>\r\n')
            for s in sList:
                __M_writer("                        <li><a href='/homepage/details/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( s.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(s.Fname))
                __M_writer('  ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(s.Lname))
                __M_writer('</a</li>\r\n')
            __M_writer('                    </ul>\r\n')
        if objectType == 'Drug':
            __M_writer('                    <ul>\r\n')
            for s in sList:
                __M_writer("                        <li><a href='/homepage/details.drugdetail/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( s.id ))
                __M_writer("'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(s.DrugName))
                __M_writer('</a></li>\r\n')
            __M_writer('                    </ul>\r\n')
        __M_writer('            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 37, "52": 3, "63": 3, "64": 9, "65": 9, "66": 15, "67": 15, "68": 20, "69": 21, "70": 22, "71": 23, "72": 23, "73": 23, "74": 23, "75": 23, "76": 23, "77": 23, "78": 25, "79": 27, "80": 28, "81": 29, "82": 30, "83": 30, "84": 30, "85": 30, "86": 30, "87": 32, "88": 34, "94": 88}}
__M_END_METADATA
"""
