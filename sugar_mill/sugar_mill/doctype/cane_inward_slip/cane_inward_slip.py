# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import string    
import random


class CaneInwardSlip(Document):
	@frappe.whitelist()
	def hdata(self):
		doc = frappe.get_all('Trip Sheet', filters={'name': self.plot_no}, fields={'name','transporter_code','transporter_name','transporter','route_name','route','distance'})
		for s in doc:
			self.transporter_code = s.transporter_code
			self.transporter_name = s.transporter_name
			self.transporter = s.transporter
			self.route_name = s.route_name
			self.route = s.route
			self.distance = s.distance
	@frappe.whitelist()
	def vivo(self):
		doc = frappe.get_all('H and T Contract', filters={'name': self.transporter_code}, fields={'name','vehicle_no','transporter_code','harvester_code','transporter_name','harvester_name','trolly_1','trolly_2','total_vehicle','vehicle_type'})
		for s in doc:
			self.transporter_name = s.transporter_name
			self.harvester_code = s.harvester_code
			self.harvester_name = s.harvester_name
			self.vehicle_type = s.vehicle_type
			self.vehicle_number = s.vehicle_no
			self.tolly_1 = s.trolly_1
			self.tolly_2 = s.trolly_2
   
	@frappe.whitelist()
	def after_save(self):
		doc1 = frappe.get_all('Branch',filters={'name':self.branch},fields=["name", "token_number",])
		for n in doc1:
			n.token_number = n.token_number + 1
			frappe.db.set_value("Branch", n.name, "token_number",n.token_number)

	# @frappe.whitelist()
	# def get_reading(self):
	# 	user=  frappe.get_all("RFID Master Setting",
    #                         fields=["rfid_machine", "idx", "date"],
    #                         filters={'rfid_operator_id': frappe.session.user},
    #                         order_by="date desc",
    #                         limit=1)
	# 	# =frappe.db.get_list("RFID Master Setting",  filters={'rfid_operator_id': frappe.session.user},fields=['rfid_machine'],)
	# 	rfid_reading=frappe.get_doc("Rfid tag Reading","rfid-tag-reading")
	# 	temp1=rfid_reading.rfid1_status
	# 	temp2=rfid_reading.rfid2_status
	# 	temp3=rfid_reading.rfid3_status
	# 	frappe.msgprint(str(user[0].rfid_machine))
	# 	if temp1=="Connected.":
	# 		self.rfid_tag=rfid_reading.rfid_1
	# 	elif temp2=="Connected.":
	# 		self.rfid_tag=rfid_reading.rfid_2
	# 	elif temp3=="Connected.":
	# 		self.rfid_tag=rfid_reading.rfid_3

	@frappe.whitelist()
	def get_reading(self):
		# Get the most recent record with 'rfid_machine' as 'RFID 2'
		user = frappe.get_all(
			"RFID Master Setting",
			fields=["rfid_machine", "idx", "date"],
			filters={
				'rfid_operator_id': frappe.session.user
			},
			order_by='date desc',
			limit=1
		)

		if not user:
			frappe.msgprint("No recent record found  for the current user.")
			return

		# Access the 'rfid_machine' and 'date' fields from the recent record
		rfid_machine = user[0].rfid_machine
		# Get the "Rfid tag Reading" document
		rfid_reading = frappe.get_doc("Rfid tag Reading", "rfid-tag-reading")

		# Get the status of RFID readers
		temp1 = rfid_reading.rfid1_status
		temp2 = rfid_reading.rfid2_status
		temp3 = rfid_reading.rfid3_status

		# Display the 'rfid_machine' value and its status
		frappe.msgprint(f"RFID Machine: {rfid_machine}")

		# Assign the appropriate value to the 'rfid_tag' variable based on the status of RFID readers
		if temp1 == "Connected." and rfid_machine == 'RFID 1':
			self.rfid_tag = rfid_reading.rfid_1
		elif temp2 == "Connected." and rfid_machine == 'RFID 2':
			self.rfid_tag = rfid_reading.rfid_2
		elif temp3 == "Connected." and rfid_machine == 'RFID 3':
			self.rfid_tag = rfid_reading.rfid_3

		doc1 = frappe.get_all("H and T Contract", fields=["name","transporter_name","vehicle_type","harvester_code","harvester_name", "rfid_tag","transporter_name"], filters={"rfid_tag": self.rfid_tag})
		found_rfid_tag = False
		for g in doc1:
			if g.rfid_tag == self.rfid_tag:
				self.rfid_tag=g.rfid_tag
				self.transporter_name=g.transporter_name
				self.vehicle_type=g.vehicle_type
				self.harvester_code=g.harvester_code
				self.harvester_name=g.harvester_name
				self.transporter_code=g.name
				frappe.msgprint(str(g.name))
				frappe.msgprint(f"RFID Tag matches with vendor {g.transporter_name}")
				found_rfid_tag = True
				break

		if not found_rfid_tag:
			frappe.throw("RFID Tag does not match with any vendor")
	
   
	# def before_save(self):
		# doc=frappe.db.get_list("Branch",filters={"branch" : self.branch},
		# 									fields=["name","cane_inward_slip_no"])
		# if(int(self.cane_inward_no)==int(0)):
		# 	self.cane_inward_no=int(doc[0].get("cane_inward_slip_no"))+1
		# 	frappe.db.set_value("Branch",doc[0].get("name"),"cane_inward_slip_no",self.cane_inward_no)
		

	# def before_save(self):
	# 	doc=frappe.db.get_list("Branch",filters={"branch" : self.branch},
	# 										fields=["name","cane_inward_slip_no"])
	# 	if(int(self.cane_inward_no)==int(0)):
	# 		self.cane_inward_no=int(doc[0].get("cane_inward_slip_no"))+1
	# 		frappe.db.set_value("Branch",doc[0].get("name"),"cane_inward_slip_no",self.cane_inward_no)
	# 	doc1= frappe.get_all("Farmer List",fields=["name","rfid_tag"],filters={"branch":self.branch})
	# 	frappe.msgprint(str(doc1))
	# 	for g in doc1:
	# 		frappe.msgprint(str(g.rfid_tag))
	# 		if g.rfid_tag==self.rfid_tag:
	# 			frappe.msgprint("RFID Tag is  match with vendor")
	# 		else:
	# 			frappe.throw("RFID Tag is dosen't match with vendor")
    
	# @frappe.whitelist()
	# def show_data(self):
	# 	doc1= frappe.get_all("Farmer List",fields=["name","rfid_tag"],filters={"branch":self.branch})
	# 	frappe.msgprint(str(doc1))
	# 	for g in doc1:
	# 		if str(g.rfid_tag) ==str(self.rfid_tag):
	# 			frappe.msgprint("RFID Tag is  match with vendor")
	# 		else:
	# 			frappe.throw("RFID Tag is dosen't match with vendor")
		# count = 0
		# for d in doc1:
		# 	if d.rfid_tag==self.rfid_tag:
		# 		count+=1
		# if count == 0:
		# 	frappe.throw(f"RFID Tag is dosen't match with vendor")

		# doc=frappe.db.get_list("Branch",filters={"branch" : self.branch},
		# 									fields=["name","cane_inward_slip_no"])
		# if(int(self.cane_inward_no)==int(0)):
		# 	self.cane_inward_no=int(doc[0].get("cane_inward_slip_no"))+1
		# 	frappe.db.set_value("Branch",doc[0].get("name"),"cane_inward_slip_no",self.cane_inward_no)
	
        
     
     
	
   
#   for i in user:
			# frappe.msgprint(str(i.rfid_machine))
		# doc=frappe.get_doc("Rfid tag Reading","rfid-tag-reading")
		# frappe.msgprint(str(doc))


	# @frappe.whitelist()
	# def vivo(self):
	# 	doc = frappe.get_all('H and T Contract', filters={'name': self.transporter_code}, fields={'name','vehicle_no','transporter_code','harvester_code','transporter_name','harvester_name','trolly_1','trolly_2','total_vehicle','vehicle_type'})
	# 	for s in doc:
	# 		self.transporter_name = s.transporter_name
	# 		self.harvester_code = s.harvester_code
	# 		self.harvester_name = s.harvester_name
	# 		self.vehicle_type = s.vehicle_type
	# 		self.vehicle_number = s.vehicle_no
	# 		self.tolly_1 = s.trolly_1
	# 		self.tolly_2 = s.trolly_2
   
	# @frappe.whitelist()
	# def slip_number(self):
	# 	self.slip_no = self.get_new_slip_number()
	# @frappe.whitelist()
	# def get_new_slip_number(self):
	# 	last_slip = frappe.db.get_value('Cane Inward Slip', filters={}, fieldname='slip_no', order_by='creation desc')
	# 	if last_slip:
	# 		new_slip = int(last_slip) + 1
	# 	else:
	# 		new_slip = 1
	# 	return str(new_slip)



			
				

