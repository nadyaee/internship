from odoo import fields, models

class City(models.Model):
    _name = 'city.city'
    name = fields.Char('City')
    state_id = fields.Many2one('state.state', 'State')

class State(models.Model):
    _name = 'state.state'
    name = fields.Char('State')
    country_id = fields.Many2one('country.country' , 'Country')

class Country(models.Model):
    _name = 'country.country'
    name = fields.Char('Country')


