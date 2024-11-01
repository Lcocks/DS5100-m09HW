#booklover_test.py
import unittest
from booklover import BookLover
#testing

class test_objectSuite(unittest.TestCase):
    """
    For testing the booklover.py file
    """
    
    def test_1_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Jane Eyre", 4)
        
        self.assertEqual(test_object.book_list.book_name[0],"Jane Eyre")
    
    def test_2_add_book(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Jane Eyre", 4)
        
        self.assertEqual(test_object.book_list.value_counts()['Jane Eyre'][4.0], 1)
    
    def test_3_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Jane Eyre", 4)
        
        self.assertEqual(test_object.has_read("Jane Eyre"), True)

    def test_4_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        self.assertFalse(test_object.has_read("Janet ErErE"))
    
    def test_5_num_books_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        
        self.assertEqual(test_object.num_books_read(), 3)
    
    def test_6_fav_books(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Nothing", 2)
        test_object.add_book("Something", 1)
        test_object.add_book("The Popol Vuh", 5)  #should not add again so 4 total; 2 above a rating of 3
        
        for i in (test_object.fav_books().book_rating > 3):
            if i == False:
                message = "The " + str(i) + " test value is not True"
                self.assertTrue(i, message)
            else:
                continue
        self.assertTrue(i)
        
if __name__ == '__main__':
    
    unittest.main(verbosity = 3)
