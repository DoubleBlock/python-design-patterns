class SensitiveInfo:
    """包含保护信息"""
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        """输出用户列表"""
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        """添加新用户到列表中"""
        self.users.append(user)
        print('Added user {}'.format(user))


class Info:
    """SensitiveInfo的保护代理"""

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        """SensitiveInfo.read()的一个包装"""
        self.protected.read()

    def add(self, user):
        """确保仅当客户端代码知道密码是才能添加用户"""
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))


if __name__ == '__main__':
    main()