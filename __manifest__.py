# -*- coding: utf-8 -*-
{
    'name': 'Factura Bs',
    'version': '10.0.0.1',
    'category': 'Custom',
    'summary': 'Factura en Bolivianos',
    'author': 'DDVC',
    'depends': ['account'],
    'data': [
        'report/report_factura_bs.xml',
        'report/report_invoice_bs.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
