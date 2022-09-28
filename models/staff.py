
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Staff(models.Model):
    _name = 'staff.staff'
    name = fields.Char('Name', required=True)
    identity =  fields.Char('Identity Number')
    departement_id = fields.Many2one('student.departement', 'Departement')
    program_id = fields.Many2one('student.program', 'Study Program')
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city_id = fields.Many2one('city.city', 'City')
    state_id = fields.Many2one('state.state',  'State')
    country_id = fields.Many2one('country.country', 'Country')
    phone = fields.Char('Phone Number')
    mobile = fields.Char('Mobile Number')
    email = fields.Char('Email')
    user_id = fields.Many2one('res.users')
    

    @api.constrains('identity')
    def check_identity(self):
        for rec in self:
            staff = self.env['staff.staff'].search([('identity', '=', rec.identity), ('id', '!=', rec.id)])
            if staff:
                raise ValidationError("Identity Number %s Already Exists" % rec.identity)
            