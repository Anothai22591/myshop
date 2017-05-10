from selenium import webdriver
import unittest
import time
    
class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        #วันหนึ่งสมศักด์หิวมากต้องการที่จะไปหาอะไรกินด้วยความที่ลิฟต์ขิงตึกนั้นเสียทำให้สมคิดไม่อยากเดินไป
        #ซื้อเอง ทัน ได้นั้นเพื่อนของเขาก็แนะนำให้ใช้ แอฟสั่งขนมและเครื่องดื่มซึ่งมีบริการส่งถึงที่เลยสมคิดจึงเข้า
        #ไปยังหน้าเว็บนั้น
        self.browser.get('http://localhost:8000')

        #เขาเห็น title หน้าเว็บเขียนไว้ว่า "Snack & Drink Delivery"  
        self.assertIn('Snack & Drink Delivery', self.browser.title)  #5
        title_text = self.browser.find_element_by_tag_name('title').text
        self.assertIn('Snack & Drink Delivery', title_text)
        time.sleep(1)
         
        #เขาพบลิงค์ login และ register เขาได้กดไปที่ register 
        link_register = self.browser.find_element_by_partial_link_text('register')
        self.assertIn('register', link_register.text)
        link_register.click()
        time.sleep(5)

        #เขาพบกับหน้า register และมีช่องกรอกข้อมูล และได้ทำการกรอกข้อมูลลงไป 
        inputbox1 = self.browser.find_element_by_id('id_Name')
        inputbox1.send_keys('anothai')
        inputbox1.send_keys(Keys.ENTER)
        
        #เขากดไปยังลิงค์ลงทะเบียน
        
        #ปรากฏช่องให้กรอก username password เมื่อกรอกเสร็จเขาจึงทำการกดลงทะเบียน
        #title_text = self.browser.find_element_by_tag_name('e').text
        #self.assertIn('e', title_text)  
#แสดงหน้าเว็บที่มีคำว่า ลงทะเบียนสำเร็จขึ้นมา ด้านล่างมีปุ่มย้อนไปหน้า login 
#เขากดไปยังลิงค์ login
        self.fail('Finish the test!')  #6 
#เขาได้พบกับหน้า login เขาจึงได้ใส่ข้อมูลไปตามที่เขาลงทะเบียนไว้ แล้วทำการกดlogin
#หน้าแสดงรายการอาหารมากมายแบ่งเป็นประเภทอยู่ตรงหน้าของเขา เขาจึงได้เลือกขนมและเครื่องดื่มที่เขาต้องการและกดปุ่มตกลงไป
#พบกับหน้าที่เเสดงรายการขนมและเครื่องดื่มที่เขาได้สั่งไป พร้อมราคาที่เขาต้องจ่าย ด้านล่างมีปุ่มยืนยันการซื้อเขาได้ทำการกดไป 
#ปรากฏคำว่าขอบคุณที่ใช้บริการขึ้นมา พร้อมลิงค์กลับไปยังหน้าแรก
if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8


