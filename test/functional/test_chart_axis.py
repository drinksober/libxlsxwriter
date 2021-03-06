###############################################################################
#
# Tests for libxlsxwriter.
#
# Copyright 2014-2017, John McNamara, jmcnamara@cpan.org
#

import base_test_class

class TestCompareXLSXFiles(base_test_class.XLSXBaseTest):
    """
    Test file created with libxlsxwriter against a file created by Excel.

    """

    def test_chart_axis01(self):
        self.run_exe_test('test_chart_axis01')

    def test_chart_axis02(self):
        self.run_exe_test('test_chart_axis02')

    def test_chart_axis04(self):
        self.run_exe_test('test_chart_axis04')

    def test_chart_axis05(self):
        self.run_exe_test('test_chart_axis05')

    def test_chart_axis06(self):
        self.run_exe_test('test_chart_axis06')

    def test_chart_axis07(self):
        self.run_exe_test('test_chart_axis07')

    def test_chart_axis08(self):
        self.run_exe_test('test_chart_axis08')

    def test_chart_axis09(self):
        self.run_exe_test('test_chart_axis09')

    def test_chart_axis10(self):
        self.run_exe_test('test_chart_axis10')

    def test_chart_axis11(self):
        self.run_exe_test('test_chart_axis11')

    def test_chart_axis12(self):
        self.run_exe_test('test_chart_axis12')

    def test_chart_axis13(self):
        self.run_exe_test('test_chart_axis13')

    # Stock chart not supported.
    # def test_chart_axis14(self):
    #     self.run_exe_test('test_chart_axis14')

    def test_chart_axis17(self):
        self.run_exe_test('test_chart_axis17')



    def test_chart_axis21(self):
        self.run_exe_test('test_chart_axis21')



    def test_chart_axis26(self):
        self.run_exe_test('test_chart_axis26')

    def test_chart_axis27(self):
        self.run_exe_test('test_chart_axis27')

    def test_chart_axis28(self):
        self.run_exe_test('test_chart_axis28')

    def test_chart_axis29(self):
        self.run_exe_test('test_chart_axis29')


    def test_chart_axis33(self):
        self.run_exe_test('test_chart_axis33')


    def test_chart_axis35(self):
        self.run_exe_test('test_chart_axis35')

    def test_chart_axis36(self):
        self.run_exe_test('test_chart_axis36')

    def test_chart_axis37(self):
        self.run_exe_test('test_chart_axis37')

    def test_chart_axis38(self):
        self.run_exe_test('test_chart_axis38')

    def test_chart_axis39(self):
        self.run_exe_test('test_chart_axis39')
