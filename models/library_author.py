from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

name = fields.Char(string='Author Name')
total_books = fields.Integer(string='Total Books')

def update_total_books(self):
    for author in self:
        author.total_books = len(self.env['library.book'].search([('author_id', '=', self.id)]))