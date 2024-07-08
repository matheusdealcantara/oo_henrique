from package.maths.controllers import Menu


def main():
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    print("O arquivo 'testbench_06.py' foi invocado como programa")
    main()
else:
    print("O arquivo 'testbench_06.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
