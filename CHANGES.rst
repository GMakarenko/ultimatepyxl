0.1.8
=====

* Added worksheet function clear_formula_values.  This deletes preset values in formulas to force recalculation, to
  solve issue in Excel 2016 not respecting force recalc flags or the absence of the calcChain.xml

0.1.5
=====

* Updated lxml writing for python3

0.1.4
=====

* Updated uuid1().get_hex() -> uuid1().hex

0.1.3
=====

* Added wb['sheetname'] notation.
* Added wb.sheetnames

0.1.2
=====

* Added ws['A1'] notation.

0.1.1
=====

* Added ws.dump() to dump all cell values.

0.1.0
=====

* Added wb.hide_sheet() / wb.unhide_sheet()

0.0.9 (unreleased)
==================

* Fixed filename parsing.

0.0.8 (unreleased)
==================

* Added function for updating formulas.

0.0.7 (unreleased)
==================

* Remove formulas from cells when setting value and remove calcChain.xml.

0.0.1 (unreleased)
==================

Initial Release
---------------

* Initial project released in Alpha.