from mock import patch
import win_HomeWin1
import unittest
import Tkinter

class HelloCallBack4TestCase_system(unittest.TestCase):
    def setUp(self):
        self.root = Tkinter.Tk()
        self.MainWindow = win_HomeWin1.MainWindow(self.root)

    def tearDown(self):
        self.root.quit()

    @patch('os.system')
    def test_helloCallBack_os_system(self, mock_tk_os_system):
        self.MainWindow.helloCallBack4()
        self.assertTrue(mock_tk_os_system.called)
        print "mock_tk_os_system_call_True"

if __name__ == '__main__':
    unittest.main()