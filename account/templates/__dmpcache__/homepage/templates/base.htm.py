# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554912205.7830443
_enable_loop = True
_template_filename = 'C:/Users/Think/tacohojo/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


from datetime import datetime

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>DMP</title>\r\n\r\n        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/css/bootstrap.min.css"></link>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/js/bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\r\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css" />\r\n\r\n    </head>\r\n    <body>\r\n        <nav class="navbar navbar-expand-lg navbar-dark bg-dark justify-content-between">\r\n            <ul class="nav navbar-nav navbar-left">\r\n                <!-- PAGE IS ')
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
        __M_writer('" href="/analytics/">Analytics</a>\r\n                </li>\r\n            </ul>\r\n            <ul class="nav navbar-nav navbar-right">\r\n                <li class="nav-item dropdown navbar-right">\r\n')
        if request.user.is_authenticated:
            __M_writer('                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                        Welcome, ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.first_name ))
            __M_writer('\r\n                    </a>\r\n')
        if not request.user.is_authenticated:
            __M_writer('                    <a class="nav-link" href="/account/login/">Login</a>\r\n')
        if request.user.is_authenticated:
            __M_writer('                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">               \r\n                        <a class="dropdown-item" href="/account/index/">Account</a>\r\n                        <div class="dropdown-divider"></div>\r\n                        <a class="dropdown-item" href="/account/logout/">Logout</a>\r\n')
        __M_writer('                    </div>\r\n                </li>\r\n            </ul>\r\n        </nav>\r\n        <header>\r\n            <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logo.png" alt="python" />\r\n            <div class="title" style="color: black"> TACOHOJO CONSULTING </div>\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n            ')
        __M_writer('\r\n            <div class="center" style="text-align:center">© Copyright Tacohojo Consulting ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(datetime.today().strftime("%Y")))
        __M_writer('. All rights reserved</div>\r\n            <div class="center" style="text-align:center">______________________</div>\r\n            \r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
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
{"filename": "C:/Users/Think/tacohojo/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 69, "20": 0, "30": 2, "31": 11, "32": 11, "33": 12, "34": 12, "35": 13, "36": 13, "37": 14, "38": 14, "39": 22, "40": 22, "41": 23, "42": 23, "43": 24, "44": 24, "45": 28, "46": 28, "47": 31, "48": 31, "49": 34, "50": 34, "51": 39, "52": 40, "53": 41, "54": 41, "55": 44, "56": 45, "57": 47, "58": 48, "59": 53, "60": 58, "61": 58, "66": 65, "67": 69, "68": 70, "69": 70, "75": 63, "81": 63, "87": 81}}
__M_END_METADATA
"""
