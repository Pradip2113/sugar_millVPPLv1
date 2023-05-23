// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cane Inward Slip', {
    transporter_code: function(frm, cdt, cdn) {
        var d = frm.doc.transporter_code
        frm.set_value('harvester_code', d);
    }
});

frappe.ui.form.on('Cane Inward Slip', {
	transporter_code: function(frm) {frm.call({
			method:'cn',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});

