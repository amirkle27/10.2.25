from template_base import DateCheck
from typing import override

class TemplateEmailInput(DateCheck):
    @override
    def get_input(self):
        print("Please enter an Email address")

    @override
    def convert_input(self,user_input):
        return str(user_input)

    @override
    def validate_data(self,data):
        at_count = data.count("@")
        at_index = data.find("@")
        dot_index = data.find(".")
        dot_spot = data.rfind(".")

        if at_count == 1 and at_index>0 and dot_index>at_index+1 and not dot_spot==0 and dot_spot<len(data)-1:
            return True


