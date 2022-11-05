def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    result = []
    for i in range(len(coordinate)):
        result.append(coordinate[i])

    return tuple(result)
    
def compare_records(azara_record, rui_record):
    str_rui = ""
    for i in rui_record[1]:
        str_rui = str_rui + i
        
    if azara_record[1] == str_rui:
        return True
    else:
        return False

def create_record(azara_record, rui_record):
    for i in rui_record[1]:
        str_rui = str_rui + i
        
    if azara_record[1] != str_rui:
        return "not a match"
    else:
        return azara_record + rui_record
    
def clean_up(combined_record_group):
    report = ""
    for i in range(len(combined_record_group)):
        new_list = list(combined_record_group[i])
        new_list.pop(1)
        report = report + str(tuple(new_list)) + "\n"

    return report
