
import interface as inter
import select_contact as s
import change_contact as change
import del_contact as delete
import export_contact as export

def action_contact(data):
    if len(data) > 1:
        selected = s.select_contact(data)
    else:
        selected = data[0]
    action = inter.action_contact()
    if action == 1:
        change.change_contact(selected)
    elif action == 2:
        delete.del_contact(selected)
    elif action == 3:
        if inter.get_type_file() == 1: export.export_contact_to_csv(selected) 
        else: export.export_contact_to_txt(selected)