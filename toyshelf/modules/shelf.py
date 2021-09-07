import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Bookcase:
    _scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]

    _creds = ServiceAccountCredentials.from_json_keyfile_name(
        './creds/toys.json', _scope
    )

    _client = gspread.authorize(_creds)
    _sheet = _client.open('Toy Inventory')

    def toys(self, shelf):
        worksheet = self._sheet.worksheet(shelf)

        records = worksheet.get_all_records()

        for record in records:
            print(record['Name'])

    def shelves(self):
        ws = self._sheet.worksheets()

        for w in ws:
            print(w.title)


Bookcase().shelves()
Bookcase().toys('Super Powers')
