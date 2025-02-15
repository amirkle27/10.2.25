from template_base import DateCheck
from typing import override

class TemplateNumberInput(DateCheck):
    @override
    def get_input(self):
        print("Please enter a number between 1 and 100")

    @override
    def convert_input(self,user_input):
        return int(user_input)

    @override
    def validate_data(self,data):
        return  1 <= data <= 100


