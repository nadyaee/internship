from odoo import models, fields, api
import time

class ReportAllTasklist(models.TransientModel):
    _name = "report.all.tasklist"

    intern_id = fields.Many2one('intern.directory', 'Name')
    date_from = fields.Date('Date from', store=True, required=True)
    date_to = fields.Date('Date to', store=True, required=True)

    def action_print_tasklist_report(self):
        data = {
            'form': self.read()[0],
            'model' : 'report.all.tasklist',
            'date_from' : self.date_from,
            'date_to' : self.date_to,
            'intern_id' : self.intern_id.id,

        }
        report_action = self.env.ref('v11_nadya_custom.action_report_tasklist').report_action(self, data=data)
        print('report', report_action)
        return report_action
    
