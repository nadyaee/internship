from odoo import fields, models

class Company(models.Model):
    _name = 'company.company'

    name = fields.Char('Name', required=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city_id = fields.Many2one('city.city', 'City')
    state_id = fields.Many2one('state.state',  'State')
    country_id = fields.Many2one('country.country', 'Country')
    phone = fields.Char('Phone Number', required=True)
    mobile = fields.Char('Mobile Number', required=True)
    email = fields.Char('Email', required=True)




