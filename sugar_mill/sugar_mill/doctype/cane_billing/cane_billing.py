# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe.model.document import Document

class CaneBilling(Document):
# ------------------------------------------------------------------------------------------------------------    
    @frappe.whitelist()
    def vivek(self):
        farmer_list_in_date = []
        doc = frappe.db.get_list("Cane Weight", fields=["farmer_name", "farmer_village", "date", "farmer_code"])
        for d in doc:
            if str(self.from_date) <= str(d.date) <= str(self.to_date):
                farmer_list_in_date.append({
                    "farmer_name": d.farmer_name,
                    "farmer_code": d.farmer_code,
                    "farmer_village": d.farmer_village,
                    "date": d.date
                })

        existing_farmer_codes = [ft.farmer_code for ft in self.farmer_table]  # Get existing farmer codes in the child table

        for farmer in farmer_list_in_date:
            if farmer["farmer_code"] not in existing_farmer_codes:
                farmer_table = self.append("farmer_table", {})
                farmer_table.farmer_name = farmer["farmer_name"]
                farmer_table.farmer_id = farmer["farmer_code"]
                farmer_table.village = farmer["farmer_village"]
                farmer_table.date = farmer["date"]
                existing_farmer_codes.append(farmer["farmer_code"])  # Add the farmer code to the existing farmer codes list

        # frappe.msgprint(str(farmer_list_in_date))

    
    # @frappe.whitelist()
    # def vivek(self):
    #     farmer_list_in_date =[]
    #     doc = frappe.db.get_list("Cane Weight",fields=["farmer_name","farmer_village","date","farmer_code"],)
    #     for d in doc:
    #         if ((str(self.from_date)<= str(d.date)<= str(self.to_date))):
    #             farmer_list_in_date.append(
    #                         {
    #                             "farmer_name": d.farmer_name,	
    #                             "farmer_code": d.farmer_code,
    #                             "farmer_village": d.farmer_village,
    #                             "date": d.date,
    #                         },
    #                     )
    #     frappe.msgprint(str(farmer_list_in_date))
    #     existing_farmer_codes = [ft.farmer_code for ft in self.farmer_table]  # Get existing farmer codes in the child table

    #     for farmer in farmer_list_in_date:
    #         if farmer["farmer_code"] not in existing_farmer_codes:
    #             farmer_table = self.append("farmer_table", {})
    #             farmer_table.farmer_name = farmer["farmer_name"]
    #             farmer_table.farmer_id = farmer["farmer_code"]
    #             farmer_table.village = farmer["farmer_village"]


        # frappe.msgprint(str(farmer_list_in_date))
        
        # for l in farmer_list_in_date:
        #     self.append("farmer_table",{
        #                         "farmer_name":l['farmer_name'],
        #                         "farmer_code":l['farmer_code'],
        #                         "farmer_village":l['farmer_village'],
        #                         "date": l['date'],
                                
        #                         }
        #                     )
        
        # child_table = frappe.get_doc("Cane Billing", self.name).farmer_table
        # for data in farmer_list_in_date:
        #     child_table.append(data)
        # self.save()
        
           
    #     parent_doc = Document({
    #         'doctype': 'Cane Billing'  # Replace 'Parent Doctype' with the actual doctype
    #     })
    #     parent_doc.child_table_fieldname = []  

    #     # Append child table entries
    #     for data in farmer_list_in_date:
    #         child_row = parent_doc.append('farmer_table', data)  # Replace 'child_table_fieldname' with the actual fieldname
    #         child_row.flags.ignore_mandatory = True

    # # Save the parent document to persist the changes
    #         parent_doc.insert()
# --------------------------------------------------------------------------------------------------------------           
    @frappe.whitelist()
    def selectall(self):
        # pass
        children = self.get("farmer_table")
        if not children:
            return
        all_selected = all([child.check for child in children])
        value = 0 if all_selected else 1
        for child in children:
            child.check = value
            
            
            
        
    @frappe.whitelist()
    def billing(self):
        # total_weight=0
        # cane_rate=4.5
        # Total_collection_amount=0
        # total_deduction=0
        for FAR in self.get("farmer_table"):
            total_weight=0
            cane_rate=4.5
            Total_collection_amount=0
            total_deduction=0
            if FAR.check:
                doc = frappe.get_all('Cane Weight', filters={'farmer_code': FAR.farmer_id}, fields={"actual_weight","farmer_code"})
                # frappe.msgprint(str(doc))
                for d in doc:
                    total_weight += int(d.actual_weight)
                    
                Total_collection_amount = total_weight * cane_rate
                # frappe.msgprint(str(total_weight))
                # frappe.msgprint(str(Total_collection_amount))
                
                
                deduction_doc = frappe.get_all('Sales Invoice', filters={'customer': FAR.farmer_id ,'status':"Unpaid"}, fields={"outstanding_amount","customer"})
                for d_d in deduction_doc:
                    total_deduction += int(d_d.outstanding_amount)
                # frappe.msgprint(str(total_deduction))
                
                
                self.append(
                    "calculation_table",
                    {
                        "farmer_name": FAR.farmer_name,
                        "farmer_id": FAR.farmer_id,
                        "village": FAR.village,
                        "total_collection_amount":Total_collection_amount ,
                        "total_deduction": total_deduction ,
                        "total_payable_amount": int(Total_collection_amount) - int(total_deduction),
                    },
                )
