from odoo import models, fields, api

class LibraryBookCategoried(models.Model):
    _inherit = 'library.book'

    category = fields.Char(string='Category', required=True )
    total_books_in_category = fields.Float(string="Total Books in Category", compute="_compute_total_in_category", store=True)

    @api.depends('category')
    def compute_total_in_category(self):
        for record in self:
            domain = [('category', '=', record.category)]
            books_in_category = self.env['library.book'].search(domain)
            record.total_books_in_category = len(books_in_category)
            
    