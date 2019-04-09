# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554837824.3185658
_enable_loop = True
_template_filename = 'C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/drugdetail.html'
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
        prescribers = context.get('prescribers', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
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
        prescribers = context.get('prescribers', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Drug Name</th>\r\n            <th>Is Opioids</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n            <tr>\r\n                <td></td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drug.DrugID.DrugName ))
        __M_writer('</td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drug.DrugID.IsOpioid ))
        __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n        </tbody> \r\n    </table>\r\n    <table class="table">\r\n        <thead>\r\n            <th></th>\r\n            <th>Top 10 Prescribers</th>\r\n            <th>Gender</th>\r\n            <th># Prescribed</th>\r\n            <th></th>\r\n        </thead>\r\n        <tbody>\r\n')
        for p in prescribers:
            __M_writer('            <tr>\r\n                <td></td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( p.PrescriberID.Lname ))
            __M_writer('</td>\r\n                <td>')
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
{"filename": "C:/Users/jhoyo/Desktop/dmp/tacohojo/homepage/templates/drugdetail.html", "uri": "drugdetail.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 14, "60": 14, "61": 15, "62": 15, "63": 29, "64": 30, "65": 32, "66": 32, "67": 32, "68": 32, "69": 33, "70": 33, "71": 34, "72": 34, "73": 38, "79": 73}}
__M_END_METADATA
"""
