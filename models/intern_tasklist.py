from odoo import fields, models, api, _

class InternTasklist(models.Model):
    _name = 'intern.tasklist'
    _rec_name="intern_id"
    _order = 'id, date desc'

    @api.model
    def default_get(self, fields):
        res = super(InternTasklist, self).default_get(fields)
        if self._context.get('active_id'):
            res['intern_id'] = self._context.get('active_id')
        return res

    date = fields.Date('Date', default=fields.Datetime.now, store=True, readonly=True)
    project_id = fields.Many2one('tasklist.project', 'Project', required=True)
    task = fields.Char('Task', required=True)
    description =  fields.Char('Description')
    intern_id = fields.Many2one('intern.directory', 'Intern Directory')



class TasklistProject(models.Model):
    _name =  'tasklist.project'

    name = fields.Char ('Name', required=True)
    description = fields.Html('Description')
    date =  fields.Date('Date', default=fields.Datetime.now, readonly=True)

