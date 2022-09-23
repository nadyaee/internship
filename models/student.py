from odoo import fields, models, api
from odoo.exceptions import ValidationError

class StudentAcademic(models.Model):
    _name = 'student.student'

    name = fields.Char('Name', required=True )
    identity_no = fields.Char('Student Number')
    departement_id =  fields.Many2one('student.departement', 'Departement')
    program_id = fields.Many2one('student.program', 'Study Program ')
    transcript = fields.Char('Transcript')

    phone = fields.Char('Phone Number')
    cv = fields.Binary('Curriculum Vitae') 
    cv_name = fields.Char()
    email = fields.Char('Email')

    date_birth = fields.Date('Date of Birth')
    city_birth_id = fields.Many2one('city.city','Place of Birth')

    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city_id = fields.Many2one('city.city', 'State')
    state_id = fields.Many2one('state.state', 'State')
    country_id = fields.Many2one('country.country', 'Country')

    identity_card = fields.Binary('Identity Card') 
    identity_card_name = fields.Char()
    family_card = fields.Binary('Family Card') 
    family_card_name = fields.Char()
    health_certificate = fields.Binary('Certificate of Health') 
    health_certificate_name = fields.Char()
    education_certificate = fields.Binary('Education Certificate') 
    education_certificate_name = fields.Char()
    skck= fields.Binary('SKCK') 
    skck_name = fields.Char()
    yellow_card = fields.Binary('Yellow Card') 
    yellow_card_name = fields.Char()
    image = fields.Binary()
    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the student terms without removing it.")
    user_id = fields.Many2one('res.users')

    @api.constrains('identity_no')
    def check_identity(self):
        for rec in self:
            student = self.env['student.student'].search([('identity_no', '=', rec.identity_no), ('id', '!=', rec.id)])
            if student:
                raise ValidationError("Identity Number %s Already Exists" % rec.identity_no)

class Departement(models.Model):
    _name = 'student.departement'
    name = fields.Char('Departement')

class Program(models.Model):
    _name = 'student.program'
    name = fields.Char('Study Program')
    departement_id = fields.Many2one('student.departement', 'Departement')



