class Animal:
    __name = None; ## __ means they are private

    def __init__(self, name):
        self.__name = name;

    def set_name(self, name):
        self.__name = name;
    def get_name(self):
        return self.__name;


cat = Animal('hukl')

print(cat.get_name());