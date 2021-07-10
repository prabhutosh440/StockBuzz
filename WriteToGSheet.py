import gspread
from oauth2client.service_account import ServiceAccountCredentials


class WriteToGSheets:

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = "C:\\Users\\PRABHU\\Downloads\\stockbuzz-319301-c3a6e5890e4d.json"
        else:
            self.file_path = file_path

    def update_to_sheet(self, df_to_sheets):

        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name(self.file_path, scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("StockBuzz")
        sheet_instance = sheet.get_worksheet(0)

        # Extract and print all of the values
        # saved_records_df = pd.DataFrame(sheet_instance.get_all_records())
        # print(saved_records_df)

        # Update sheets with the new dataframe

        sheet_instance.update([df_to_sheets.columns.values.tolist()] + df_to_sheets.values.tolist())
