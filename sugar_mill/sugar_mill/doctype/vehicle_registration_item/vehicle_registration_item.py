# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate, date_diff

class VehicleRegistrationitem(Document):
    @frappe.whitelist()
    def slip_number(self):
        frappe.msgprint("kkkoooo")
        self.slip_no = self.get_new_slip_number()
    @frappe.whitelist()
    def get_new_slip_number(self):
        last_slip = frappe.db.get_value('Vehicle Registration item', filters={}, fieldname='cart_no', order_by='creation desc')
        if last_slip:
            new_slip = int(last_slip) + 1
        else:
            new_slip = 1
        return str(new_slip)
