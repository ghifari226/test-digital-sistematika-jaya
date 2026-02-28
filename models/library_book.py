from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title')
    author_id = fields.Many2one('library.author', string='Author')
    price = fields.Float(string='Price')