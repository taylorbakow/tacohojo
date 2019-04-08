# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554756898.866115
_enable_loop = True
_template_filename = 'C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>DMP</title>\r\n\r\n        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/css/bootstrap.min.css"></link>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/js/bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\r\n\r\n    </head>\r\n    <body>\r\n        <nav class="navbar navbar-expand-lg navbar-dark bg-dark justify-content-between">\r\n            <ul class="nav navbar-nav navbar-left">\r\n                <!-- PAGE IS ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.dmp.page ))
        __M_writer(' -->\r\n                <a href="/" class="navbar-left"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/Logo.png" style="width:50px; height:40px; margin-right:10px;"></a>\r\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'index' else ''))
        __M_writer('">\r\n                    <a class="nav-link" href="/">Home</a>\r\n                </li>\r\n                <li class="nav-item">\r\n                    <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'about' else ''))
        __M_writer('" href="/about/">About</a>\r\n                </li>\r\n                <li class="nav-item">\r\n                    <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'contact' else ''))
        __M_writer('" href="/contact/">Contact</a>\r\n                </li>\r\n                <li class="nav-item">\r\n                    <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'analytics' else ''))
        __M_writer('" href="/analytics/">Analytics</a>\r\n                </li>\r\n            </ul>\r\n            <ul class="nav navbar-nav navbar-right">\r\n                <li class="nav-item"><a class="nav-link" href="/account/login/">Login</a></li>\r\n            </ul>\r\n        </nav>\r\n        <header>\r\n            <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logo.png" alt="python" />\r\n            <div class="title" style="color: black"> TACOHOJO CONSULTING </div>\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer style="text-align: center">\r\n            <h2>Footer</h2>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "28": 2, "29": 11, "30": 11, "31": 12, "32": 12, "33": 13, "34": 13, "35": 14, "36": 14, "37": 21, "38": 21, "39": 22, "40": 22, "41": 23, "42": 23, "43": 27, "44": 27, "45": 30, "46": 30, "47": 33, "48": 33, "49": 41, "50": 41, "55": 48, "61": 46, "67": 46, "73": 67}}
__M_END_METADATA
"""
