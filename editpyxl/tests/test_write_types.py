import os
from datetime import date
from unittest import TestCase

from editpyxl.workbook import Workbook


class WriteTypesTestCase(TestCase):

    def setUp(self) -> None:
        self.xl_path = "editpyxl/tests/xl.xlsx"
        self.test_xl_path = "editpyxl/tests/test_xl.xlsx"
        wb = Workbook()
        self.wb = wb.open(self.xl_path)

    def tearDown(self) -> None:
        os.remove(self.test_xl_path)

    def test_writes_dates(self):
        dt = date(year=1900, month=12, day=13)

        ws = self.wb["Sheet1"]
        ws["C1"] = dt

        self.wb.save(self.test_xl_path)
        self.wb.close()

        new_wb = Workbook().open(self.test_xl_path)
        ws = new_wb["Sheet1"]

        self.assertEqual("348.0", ws["C1"].value)
        new_wb.close()
