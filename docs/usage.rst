Simple usage
=======================

Edit a workbook
------------------
::

    from editpyxl import Workbook

    wb = Workbook()

    source_filename = r'file_to_edit.xlsx'

    wb.open(source_filename)

    ws = wb.active

    ws.cell('A1').value = 3.14

    wb.save(destination_filename)

    wb.close()

