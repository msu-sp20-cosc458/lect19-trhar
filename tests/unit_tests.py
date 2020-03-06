import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("!! Purple ")
        self.assertEqual(response, "Oops! I didn't recognize your command :(")
        
    def test_add_command(self):
        response = functions.get_chatbot_response("!! add 8 2")
        self.assertEqual(response,10)
    
    def test_divide_command(self):
        response = functions.get_chatbot_response("!! divide 8 2")
        self.assertEqual(response,4)
    
    def test_hey_command(self):
        response = functions.get_chatbot_response("!! Hey ")
        self.assertEqual(response,"What's up!")
    
    def test_say_command(self):
        response = functions.get_chatbot_response("!! say Hello World!")
        self.assertEqual(response,"Hello World!")
    
    def test_regular_strings(self):
        response = functions.get_chatbot_response("blah blah")
        self.assertEqual(response,'')
    

if __name__ == '__main__':
    unittest.main()
