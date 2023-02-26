
class AuthEmail:
    email = 'Введите валидный адрес электронной почты'
    password = 'Введите валидный пароль'


class AuthPhone:
    phone = 'Введите валидный номер телефона'
    password = 'Введите валидный пароль'


class AuthLogin:
    login = 'Введите валидный логин'
    password = 'Введите валидный пароль'


class InvalidData:
    login = '7555555test'
    password = "7555555test55557"


class SymbolData:
    login = ')(*&^$!@#!'
    password = "*&$!@#!"


class CyrillicData:
    login = 'Логин'
    password = "Пароль"


class LongData:
    login = 'test'
    password = "test"
