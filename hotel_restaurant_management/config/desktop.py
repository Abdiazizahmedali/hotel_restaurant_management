from frappe import _

def get_data():
    return [
        {
            "module_name": "Restaurant",
            "color": "orange",
            "icon": "octicon octicon-device-desktop",
            "type": "module",
            "label": _("Restaurant")
        },
        {
            "module_name": "Hotel",
            "color": "blue",
            "icon": "octicon octicon-home",
            "type": "module",
            "label": _("Hotel")
        }
    ] 