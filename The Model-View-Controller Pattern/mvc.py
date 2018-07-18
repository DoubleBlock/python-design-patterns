quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    """名言模型"""
    def get_quote(self, n):
        """获取名言"""
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:
    """视图"""
    def show(self, quote):
        """展示名言"""
        print('the quote is: "{}"'.format(quote))

    def error(self, msg):
        """输出错误消息"""
        print('Error: {}'.format(msg))

    def select_quote(self):
        """读取用户选择"""
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    """负责协调模型和视图"""
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        """校验用户提供的名言索引，然后从模型中获取名言，并返回给视图展示"""
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
            else:
                valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()