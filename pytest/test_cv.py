from pyresparser import ResumeParser
import unittest
import jdcv 

class TestCV(unittest.TestCase):

    def test_cv_skill(self):
        fps = ["pytest/cv-pdf/p4.pdf", "pytest/cv-pdf/p7.pdf"]
        for fp in fps :
            data = ResumeParser(fp).get_extracted_data()
            print(data)
            self.assertTrue(len(data['skills'])>1)
            
            # cvr =jdcv.CVReader()
            # cv , _, _, _ = cvr.read_cv(fp)
            # sum_s = cvr.match_cv_skill( cv)
            # print( sum_s )
            # self.assertTrue(len(sum_s)>1)    
        
if __name__ == '__main__':
    unittest.main()
