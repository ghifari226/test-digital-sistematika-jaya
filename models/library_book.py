from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title')
    author_id = fields.Many2one('library.author', string='Author')
    price = fields.Float(string='Price')
    
    @api.constrains('price')
    def _non_negative_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Price can not be negative.")