# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521153919.9427915
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/catalog/templates/index.products.html'
_template_uri = 'index.products.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <ul class="product_list">\r\n')
        for s in products:
            __M_writer('        <li>\r\n            <div class="price">')
            __M_writer(str(s.price))
            __M_writer('</div>\r\n            <div class="pics"><a href="/catalog/details/')
            __M_writer(str(s.id))
            __M_writer('/"><img src=')
            __M_writer(str(s.image_url()))
            __M_writer('></a></div>\r\n            <div class = "name"><a href="#">')
            __M_writer(str(s.name))
            __M_writer('</a></div>\r\n        </li>\r\n')
        __M_writer('    </ul>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/catalog/templates/index.products.html", "uri": "index.products.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 15, "48": 3, "55": 3, "56": 6, "57": 7, "58": 8, "59": 8, "60": 9, "61": 9, "62": 9, "63": 9, "64": 10, "65": 10, "66": 13, "72": 66}}
__M_END_METADATA
"""
