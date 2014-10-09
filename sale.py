# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['Sale', 'SaleTypifiedDescription', 'SaleLine',
    'SaleLineTypifiedDescription']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    descriptions = fields.Many2Many('sale.order-typified.description', 'sale',
        'description', 'Descriptions')


class SaleTypifiedDescription(ModelSQL):
    'Sale Order - TypifDescription'
    __name__ = 'sale.order-typified.description'

    sale = fields.Many2One('sale.sale', 'Sale', ondelete='CASCADE',
        required=True, select=True)
    description = fields.Many2One('typified.description',
        'Typified Description', ondelete='CASCADE', required=True, select=True)


class SaleLine:
    __name__ = 'sale.line'

    descriptions = fields.Many2Many('sale.line-typified.description', 'line',
        'description', 'Descriptions')


class SaleLineTypifiedDescription(ModelSQL):
    'Sale Line - TypifDescription'
    __name__ = 'sale.line-typified.description'

    line = fields.Many2One('sale.line', 'Sale Line', ondelete='CASCADE',
        required=True, select=True)
    description = fields.Many2One('typified.description',
        'Typified Description', ondelete='CASCADE', required=True, select=True)
