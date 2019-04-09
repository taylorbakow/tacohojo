# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554840696.328358
_enable_loop = True
_template_filename = 'C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/drugdetail.html'
_template_uri = 'drugdetail.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        group = context.get('group', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        drug = context.get('drug', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        group = context.get('group', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        drug = context.get('drug', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Drug Name</th>\r\n            <th>Is Opioids</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n            <tr>\r\n                <td></td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drug.DrugID.DrugName ))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drug.DrugID.IsOpioid ))
        __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n        </tbody> \r\n    </table>\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Top 10 Prescribers</th>\r\n            <th>Gender</th>\r\n            <th># Prescribed</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n')
        for p in prescribers:
            __M_writer('            <tr>\r\n                <td></td>\r\n')
            if group.name == 'Health Officials':
                __M_writer('                    <td><a href="/homepage/details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer('"> ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Fname ))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Lname ))
                __M_writer('</a></td>\r\n')
            elif group.name == 'Data Clerks':
                __M_writer('                    <td><a href="/homepage/details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer('"> ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Fname ))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Lname ))
                __M_writer('</a></td>\r\n')
            elif group.name == 'Prescribers':
                __M_writer('                    <td><a href="/homepage/details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.id ))
                __M_writer('">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.id ))
                __M_writer('</a></td>\r\n')
            __M_writer('                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Gender ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.QtyPrescribed ))
            __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n')
        __M_writer('        </tbody> \r\n    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Taylo/github/tacohojo/tacohojo/homepage/templates/drugdetail.html", "uri": "drugdetail.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 14, "62": 14, "63": 15, "64": 15, "65": 29, "66": 30, "67": 32, "68": 33, "69": 33, "70": 33, "71": 33, "72": 33, "73": 33, "74": 33, "75": 34, "76": 35, "77": 35, "78": 35, "79": 35, "80": 35, "81": 35, "82": 35, "83": 36, "84": 37, "85": 37, "86": 37, "87": 37, "88": 37, "89": 39, "90": 39, "91": 39, "92": 40, "93": 40, "94": 44, "100": 94}}
__M_END_METADATA
"""
