from odoo import fields, models, api,  _ 
from dateutil.relativedelta import relativedelta

class InternDirectory(models.Model):
    _name = 'intern.directory'
    _rec_name = 'student_id'
    _order = 'id desc'
    
    sequence = fields.Char(string='Reference', default=lambda self: _('New'),
        copy=False, readonly=True, required=True)
    student_id = fields.Many2one( 'student.student', 'Student', required=True, readonly=True)
    intern_identity = fields.Char('Student Identity', related="student_id.identity_no", readonly=True)
    departement_id = fields.Many2one(readonly=True, related='student_id.departement_id')
    program_id = fields.Many2one('student.program', readonly=True, related='student_id.program_id')
    company_id = fields.Many2one('company.company', 'Company', required=True, readonly=True)
    start_date = fields.Date('Start Date', readonly=True)
    end_date = fields.Date('End Date', readonly=True)
    duration = fields.Char('Duration (Month)', compute="_compute_duration", store=True)
    supervisor = fields.Char('Supervisor')
    departement = fields.Char('Departement')
    position = fields.Char('Position')
    job_scope_ids = fields.One2many('job.scope', 'intern_id', store=True)
    submission_id = fields.Many2one('submission.submission', readonly=True)
    intern_takslist_ids = fields.One2many('intern.tasklist', 'intern_id', store=True)

    @api.multi
    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for emp in self:
            duration = relativedelta(fields.Datetime.from_string(emp.end_date), fields.Datetime.from_string(emp.start_date))
            emp.duration = str(duration.months)

    @api.model
    def create(self, vals):
        if 'sequence' not in vals or vals['sequence'] == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('intern.directory') or _('New')
        res = super(InternDirectory, self).create(vals)
        return res
    

class JobScope(models.Model):
    _name = 'job.scope'
    
    name = fields.Char()
    description = fields.Char('Description')
    intern_id = fields.Many2one('intern.directory', 'Intern Directory')

