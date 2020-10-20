# 1. Описати атрибут ip за допомогою дескрипторів.
#     атрибут може бути встановленим лише якщо значення - str,
#     відповідає шаблону "x.x.x.x" та кожен блок може бути конвертований в int
# 2. Створити ssh объект та викликати метод connect (імітація підключення)
# 3. Змінити доступ до методу execute. Якщо  self.connected == False має викликатися метод wait_for_connection (імітіція перепідключення),
#   якщо підключення встановлено має спрацювати метод execute.


class IP_Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        try:
            assert len([int(i) for i in value.split(".")]) == 4
        except AssertionError:
            raise ValueError("IP address must consist of 4 octets")
        except ValueError:
            raise ValueError("IP address's octets must be integers from 0 to 255")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class SSH():
    ip = IP_Descriptor('ip')

    def __init__(self, ip):
        self.ip = ip
        self.connected = False

    def __getattr__(self, item):  # for not implemented attributes only
        print('Get attr {}'.format(item))
        return 'not implemented'

    def __getattribute__(self, item):
        if item == "execute":
            if not self.connected:
                self.wait_for_connection(10)
            if self.connected:
                return super().__getattribute__(item)
            raise ConnectionError
        else:
            print("Get attribute: {}".format(item))
            return super().__getattribute__(item)

    def connect(self):
        # Connection via supported connection type
        # password = getpass.getpass()
        # create connection to host
        self.connected = True

    def close_connection(self):
        # Close supported connection type
        self.connected = False

    def wait_for_connection(self, timeout, polling=0.1):
        print('wait for connection..')

    def execute(self, timeout, polling=0.1):
        print('wait for execution..')


if __name__ == "__main__":
    s = SSH("8.8.8.8")
    s.execute(1)  # raises Connection error
    s.connect(1)
    s.execute(1)