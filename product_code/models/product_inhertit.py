from odoo import models, fields, api

class CategoryInherit(models.Model):
    _inherit = 'product.category'

    code = fields.Char(string="Code", size=5)



class ProductInherit(models.Model):
    _inherit = 'product.product'

    code_id = fields.Char(string="Code Id", related='categ_id.code')


    @api.model
    def create(self, vals):
        if 'categ_id' in vals:
            category = self.env['product.category'].browse(vals['categ_id'])
            code_details = str(category.code)

            sequence_number = self.env['product.product'].search_count([
                ('categ_id', '=', category.id),
            ]) + 1

            vals['default_code'] = code_details + str(sequence_number)

        return super(ProductInherit, self).create(vals)







