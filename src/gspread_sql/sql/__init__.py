
def connect(spreadsheet_id, sheet_name):
    from .client import Connection

    return Connection(spreadsheet_id, sheet_name)