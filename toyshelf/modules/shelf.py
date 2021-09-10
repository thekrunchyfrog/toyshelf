import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials


class Bookcase:
    _scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]

    _creds = ServiceAccountCredentials.from_json_keyfile_name(
        'toyshelf/creds/toys.json', _scope
    )

    _client = gspread.authorize(_creds)
    _sheet = _client.open('Toy Inventory')

    def toys(self, shelf):
        toys = []
        worksheet = self._sheet.worksheet(shelf)

        records = worksheet.get_all_records()

        for record in records:
            toys.append(
                {
                    'name': record['Name'],
                    'complete': record['Complete'],
                    'notes': record['Notes'],
                }
            )

        return json.dumps(toys)

    def shelves(self):
        toy_lines = []
        ws = self._sheet.worksheets()

        for w in ws:
            toy_lines.append({'shelf': w.title})

        return json.dumps(toy_lines)
