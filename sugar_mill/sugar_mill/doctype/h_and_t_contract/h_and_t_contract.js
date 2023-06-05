// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

// frappe.ui.form.on('H and T Contract', {
// 	on_update: function(frm) {
// 		frm.call({
// 			method:'update_event',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
		
// 	}
// });
// Filter for Harvester on H and T Contract
frappe.ui.form.on("H and T Contract", {
    refresh: function(frm) {
        // if (frm.doc.isfarmer == 1) { // Replace with the name of the checkbox field
            frm.set_query("harvester_code", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Farmer List", "is_harvester", '=', 1] // Replace with your actual filter criteria
                    ]
                };
            });
        // }
    }
});

frappe.ui.form.on("H and T Contract", {
    refresh: function(frm) {
        // if (frm.doc.isfarmer == 1) { // Replace with the name of the checkbox field
            frm.set_query("transporter_code", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Farmer List", "is_transporter", '=', 1] // Replace with your actual filter criteria
                    ]
                };
            });
        // }
    }
});
  
