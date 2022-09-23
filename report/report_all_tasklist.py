from datetime import datetime, timedelta
from odoo import api, fields,  models, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

class RecapReportAllTasklist(models.AbstractModel):
    _name = "report.v11_internship.report_all_tasklist"

    @api.model
    def get_report_values(self, docids, data=None):
        domain = []
        if data.get('date_from'):
            domain.append(('date', '>=', data.get('date_from')))
        if data.get('date_to'):
            domain.append(('date', '<=', data.get('date_to')))
        if data.get('intern_id'):
            domain.append(('intern_id', '=', data.get('intern_id')))
        docs = self.env['intern.tasklist'].search(domain)
        tasklist = data['form']['intern_id'][1]
        data.update({'tasklists': tasklist})
        print('result 3 :' , data)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'intern.tasklist',
            'docs': docs,
            'datas': data
        }
