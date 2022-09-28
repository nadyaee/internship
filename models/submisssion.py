from odoo import fields, models, api,  _ 
from dateutil.relativedelta import relativedelta

class Submission(models.Model):
    _name = 'submission.submission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'
    _order = 'id desc'


    sequence1 = fields.Char(string='Sumbission Reference', default=lambda self: _('New'),
        copy=False, readonly=True, required=True,
        states={'done': [('readonly', True)]}, track_visibility='always')
    sequence2 = fields.Char(string='Cover Letter Reference', default=lambda self: _('New'),
        copy=False, readonly=True, required=True,
        states={'done': [('readonly', True)]}, track_visibility='always')
    
    company_id = fields.Many2one('company.company', required=True)
    company_street = fields.Char('Street', readonly=True, related='company_id.street')
    company_street2 = fields.Char('Street2', readonly=True, related='company_id.street2')
    company_city_id = fields.Many2one('city.city', 'City', readonly=True, related='company_id.city_id')
    company_zip = fields.Char('Zip', readonly=True, related='company_id.zip')
    company_state_id = fields.Many2one('state.state', 'State', readonly=True, related='company_id.state_id')
    company_country_id = fields.Many2one('country.country', 'Country', readonly=True, related='company_id.country_id')
    company_phone = fields.Char('Phone Number', readonly=True, related='company_id.phone')
    company_mobile = fields.Char('Mobile Number', readonly=True, related='company_id.mobile')
    submisison_date =  fields.Date(string='Create Date', default=fields.Datetime.now, readonly=True, index=True,  required=True)
    letter_date =  fields.Date(string='Create Date', default=fields.Datetime.now, readonly=True, index=True,  required=True)
    state = fields.Selection([('draft', 'Draft'), ('submit', 'Submit'), ('progres', 'On Going'), ('done', 'Done'),   ('cancel', 'Cancelled'), ], required=True, default='draft', 
    help=" * The 'Draft' status is used when a student is encoding a create new submission and unsubmit Submission.\n"
             " * The 'Submit' status is used when a student is submit Submission. It stays in the Submit status till the staff validate the submission.\n"
             " * The 'On Going' status is used when staff validate Submission. It stays in the On Going status till the student confirmed the internship accepted.\n"
             " * The 'Done' status is set automatically when the student confirmed Submission .\n"
             " * The 'Cancelled' status is used when student cancel Submission when the internship rejected.", track_visibility='always')
    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the submission terms without removing it.")
    student_id = fields.Many2one('student.student', 'Student', required=True)
    identity = fields.Char('Student Number', readonly=True, related='student_id.identity_no')
    departement_id = fields.Many2one(readonly=True, related='student_id.departement_id')
    program_id = fields.Many2one('student.program', readonly=True, related='student_id.program_id')
    start_date =  fields.Date('Start Date')
    end_date =  fields.Date('End Date')
    duration = fields.Char('Duration (Month)', compute="_compute_duration",store=True)
    staff_id = fields.Many2one('staff.staff', required=True)
    path = fields.Selection(
        [('independent', 'Independent'),
         ('collaboration', 'Collaboration'),
        ], string='Path')
        
    @api.model
    def create(self, vals):
        if 'sequence1' not in vals or vals['sequence1'] == _('New'):
            vals['sequence1'] = self.env['ir.sequence'].next_by_code('submission.submission1') or _('New')
        if 'sequence2' not in vals or vals['sequence2'] == _('New'):
            vals['sequence2'] = self.env['ir.sequence'].next_by_code('submission.submission2') or _('New')
        res = super(Submission, self).create(vals)
        return res

    def action_print_submission(self):
        return self.env.ref('v11_nadya_custom.report_submission_letter').report_action(self)
    def action_print_cover(self):
        return self.env.ref('v11_nadya_custom.report_cover_letter').report_action(self)
    def action_submit(self):
        for rec in self:rec.state= 'submit'
    def action_validate(self):
        for rec in self:rec.state= 'progres'
    def action_confirm(self):
        for rec in self:rec.state= 'done'
    def action_cancel(self):
        for rec in self:rec.state= 'cancel'

    @api.multi
    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for emp in self:
            duration = relativedelta(fields.Datetime.from_string(emp.end_date), fields.Datetime.from_string(emp.start_date))
            emp.duration = (duration.months) 

    @api.multi
    def write(self,values):
        record = super(Submission, self).write(values)
        if 'state' in values and values.get('state') == 'done':
            self.env['intern.directory'].create({
                'submission_id' : self.id,
                'company_id' : self.company_id.id,
                'student_id' : self.student_id and self.student_id.id or False,
                'start_date' : self.start_date,
                'end_date' : self.end_date,       
                
            })
        return record

