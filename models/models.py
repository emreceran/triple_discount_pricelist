from odoo import fields, models, api

class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    discount1 = fields.Float(string="Discount 1 (%)", default=0.0)
    discount2 = fields.Float(string="Discount 2 (%)", default=0.0)
    discount3 = fields.Float(string="Discount 3 (%)", default=0.0)

    @api.onchange('discount1', 'discount2', 'discount3')
    def _onchange_discounts(self):
        for item in self:
            # Üst üste yüzde şeklinde indirimlerin hesaplanması
            price_after_discount1 = (1 - item.discount1 / 100)
            price_after_discount2 = price_after_discount1 * (1 - item.discount2 / 100)
            total_discount = 1 - (price_after_discount2 * (1 - item.discount3 / 100))
            item.percent_price = total_discount * 100
