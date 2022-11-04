def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    result = []
    for i in range(len(coordinate)):
        result.append(coordinate[i])

    return tuple(result)
    
def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    str_rui = ""
    for i in rui_record[1]:
        str_rui = str_rui + i
        
    if azara_record[1] == str_rui:
        return True
    else:
        return False

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    str_rui = ""
    for i in rui_record[1]:
        str_rui = str_rui + i
        
    if azara_record[1] != str_rui:
        return "not a match"
    else:
        return azara_record + rui_record
    
def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ""
    for i in range(len(combined_record_group)):
        new_list = list(combined_record_group[i])
        new_list.pop(1)
        report = report + str(tuple(new_list)) + "\n"

    return report
