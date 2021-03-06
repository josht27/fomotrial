# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522730866.3483315
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/catalog/templates/details.html'
_template_uri = 'details.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['top_center', 'content_center']


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
    return runtime._inherit_from(context, 'app_base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        myPics = context.get('myPics', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <!--Page Title-->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        myPics = context.get('myPics', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n\r\n    <div id='image_container'>\r\n        <ul id='thumbnails'>\r\n")
        for p in myPics:
            __M_writer('                <li class =\'image\' alt="Thumbnail Images"><img src=\'')
            __M_writer(str(p))
            __M_writer("'></li>\r\n")
        __M_writer('         </ul>\r\n         <img id=\'largeimage\' alt="Image of ')
        __M_writer(str(product.name))
        __M_writer('" src=\'')
        __M_writer(str(product.image_url()))
        __M_writer('\'>\r\n     </div>\r\n     <div id=\'product_details\'>\r\n         <h1 class="title">')
        __M_writer(filters.html_escape(str(product.name)))
        __M_writer("</h1>\r\n         </br>\r\n\r\n        <div class ='description'>")
        __M_writer(str(product.description))
        __M_writer("</div>\r\n        <div class ='price'>$")
        __M_writer(str(product.price))
        __M_writer(" each</div>\r\n\r\n     <!--if product.__class__.__name__ == 'BulkProduct':-->\r\n           ")
        __M_writer(str( form ))
        __M_writer('\r\n     <!--endif-->\r\n\r\n\r\n     </div>\r\n</br></br></br></br></br></br></br></br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/catalog/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 6, "51": 33, "57": 4, "63": 4, "69": 8, "78": 8, "79": 13, "80": 14, "81": 14, "82": 14, "83": 16, "84": 17, "85": 17, "86": 17, "87": 17, "88": 20, "89": 20, "90": 23, "91": 23, "92": 24, "93": 24, "94": 27, "95": 27, "101": 95}}
__M_END_METADATA
"""
