// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Add To Sampling', {
	issue_list: function(frm) {
		frm.clear_table("cane_master_data")
		frm.refresh_field('cane_master_data')
		frm.call({
			method: 'list',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});

// frappe.ui.form.on('Add To Sampling', {
// 	check: function(frm) {
// 		frm.call({
// 			method:'vivek',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
		
// 	}
// });

// frappe.ui.form.on('Add To Sampling', {
// 	add_for_sampling: function(frm) {
// 		frm.clear_table("selected_for_crop_sampling")
// 		frm.refresh_field('selected_for_crop_sampling')
// 		frm.call({
// 			method: 'mist',//function name defined in python
// 			doc: frm.doc, //current document
// 		});

// 	}
// });

frappe.ui.form.on('Add To Sampling', {
	check: function(frm) {
		frm.call({
			method: 'selectall',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});



