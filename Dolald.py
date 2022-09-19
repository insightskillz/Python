class Duck:
    def __init__(self, value):
        self._v = value
    def quack(self):
        print('Quaack!', self._v)

    def walk(self):
        print('Walks like a duck', self._v)


def main():
    donald = Duck(45)
    donald.quack()
    donald.walk()


if __name__=="__main__":main()
