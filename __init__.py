# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .typified import *
from .sale import *


def register():
    Pool.register(
        Category,
        Description,
        SaleTypifiedDescription,
        SaleLineTypifiedDescription,
        Sale,
        SaleLine,
        module='sale_typified_description', type_='model')
