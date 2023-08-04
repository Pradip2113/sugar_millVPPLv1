# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SlipBoyAssignment(Document):
	@frappe.whitelist()
	def before_save(self):
		for s in self.get("villages"):
			user_permission = frappe.new_doc('User Permission')
			user_permission.user = self.user
			user_permission.allow = 'Village'
			user_permission.for_value = s.village
			user_permission.insert()
			user_permission.save()



	# s=frappe.new_doc('User Permission')
	# s.user=doc.user
	# s.allow="Village"
	# s.for_value=doc.village
	# s.insert()