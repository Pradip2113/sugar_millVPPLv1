// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

// frappe.ui.form.on('H and T Contract', {
// 	after_save: function(frm) {
// 		frm.call({
// 			method:'eeeuu',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
		
// 	}
// });

frappe.ui.form.on('H and T Contract', {
    after_save: function(frm) {
        var fieldValueexist = frappe.model.get_value("H and T Contract", frm.doc.name, 'new_h_t_no');
         if (fieldValueexist) {
    console.log("Field has a value");
  }
  else
  {
        var fieldName = 'new_h_t_no';
        var fieldValue = frm.doc.name.substring(10);
        frappe.db.set_value('H and T Contract', frm.doc.name, fieldName, fieldValue)
    .then(() => {
        setTimeout(function() {
            frm.reload_doc();
        }, 1000); 
    })
    .catch((error) => {
        console.log('Error updating field value:', error);
    });
}   
    }
});

// Filter for Harvester on H and T Contract
frappe.ui.form.on("H and T Contract", {
    refresh: function(frm) {
        // if (frm.doc.isfarmer == 1) { // Replace with the name of the checkbox field
            frm.set_query("harvester_code", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Farmer List", "is_harvester", '=', 1],
                        ["Farmer List", "workflow_state", '=', 'Approved']// Replace with your actual filter criteria
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
                        ["Farmer List", "is_transporter", '=', 1],
                        ["Farmer List", "workflow_state", '=', 'Approved'] // Replace with your actual filter criteria
                    ]
                };
            });
        // }
    }
});

frappe.ui.form.on('H and T Contract', {
	old_no: function(frm) {
		frm.call({
			method:'oldhandtcode',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});

frappe.ui.form.on("H and T Contract", {
    refresh: function(frm) {
     
            frm.set_query("old_no", function() { 
                return {
                    filters: [
                        ["H T Master", "hts", '!=', frm.doc.season],
                    ]
                };
            });
    }
});

