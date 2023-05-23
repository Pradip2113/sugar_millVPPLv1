# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate, date_diff

class VehicleRegistrationitem(Document):
    @frappe.whitelist()
    def calculate_days(self):
        frappe.msgprint("jhsdfgjksdgaw")
        self.no_of_days = date_diff(self.submit_date, self.issue_date)
