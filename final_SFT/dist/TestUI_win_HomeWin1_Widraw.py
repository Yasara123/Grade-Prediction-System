from mock import patch
import win_HomeWin1
import unittest
import Tkinter

class HelloCallBack4TestCase_withdraw(unittest.TestCase):
    def setUp(self):
        self.root = Tkinter.Tk()
        self.MainWindow = win_HomeWin1.MainWindow(self.root)

    def tearDown(self):
        self.root.quit()

    @patch('Tkinter.Tk.withdraw')
    def test_helloCallBack4_withdraw(self, mock_tk_withdraw):
        self.MainWindow.helloCallBack4()
        self.assertTrue(mock_tk_withdraw.called)
        print "mock_tk_os_widraw_call_True"

if __name__ == '__main__':
    unittest.main()