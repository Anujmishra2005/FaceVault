from datetime import datetime
import openpyxl
import os

class Logger:
    def __init__(self, filename="vault_log.xlsx"):
        self.filename = filename
        if not os.path.exists(self.filename):
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Log"
            ws.append(["Name", "Action", "Timestamp"])
            wb.save(self.filename)

    def log_action(self, name, action):
        wb = openpyxl.load_workbook(self.filename)
        ws = wb["Log"]
        ws.append([name, action, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        wb.save(self.filename)
