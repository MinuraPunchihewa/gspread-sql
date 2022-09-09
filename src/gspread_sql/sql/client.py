
class Connection:
    def __init__(self, spreadsheet_id, sheet_name):
        self.query_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?sheet={sheet_name}"

