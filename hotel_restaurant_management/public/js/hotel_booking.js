frappe.pages['hotel-booking'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Hotel Booking',
        single_column: true
    });

    $(frappe.render_template('hotel_booking', {})).appendTo(page.body);

    // JS logic for fetching rooms, handling booking creation will go here
    // (see hotel_booking.html for UI structure)
}; 