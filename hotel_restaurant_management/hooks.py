app_name = "hotel_restaurant_management"
app_title = "Hotel & Restaurant Management"
app_publisher = "Your Name"
app_description = "Comprehensive Restaurant and Hotel Management for ERPNext v15"
app_icon = "octicon octicon-home"
app_color = "blue"
app_email = "your@email.com"
app_license = "MIT"

# Includes in fixtures
fixtures = [
    "Workflow",
    "Report"
]

# App modules
app_include_js = [
    "/assets/hotel_restaurant_management/js/restaurant_order.js",
    "/assets/hotel_restaurant_management/js/hotel_booking.js"
]
app_include_css = []

# Document Events, Scheduled Tasks, etc. can be added as needed 