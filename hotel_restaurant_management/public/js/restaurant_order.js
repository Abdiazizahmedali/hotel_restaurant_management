frappe.pages['restaurant-order'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Restaurant Order',
        single_column: true
    });

    $(frappe.render_template('restaurant_order', {})).appendTo(page.body);

    // JS logic for fetching tables, menu, and handling order creation will go here
    // (see restaurant_order.html for UI structure)
}; 