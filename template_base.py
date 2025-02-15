from abc import ABC, abstractmethod


class DateCheck(ABC):
    def check_input(self):
        while True:
            self.get_input()
            user_input = input("")
            if not user_input:
                print("Input can't be empty. Please try again")
                continue
            try:
                data = self.convert_input(user_input)
            except ValueError:
                print("Invalid type, Please try again")
                continue
            if self.validate_data(data):
                print("Good Job, nicely done!")
                return data
            else:
                print("Invalid data, please try again!")
                continue


    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def convert_input(self,user_input):
        pass

    @abstractmethod
    def validate_data(self,data):
        pass
