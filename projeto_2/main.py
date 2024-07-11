# Autor: Matheus de Alcântara
from package.maths.controllers import Menu


def workspace():
    input("Pressione Enter para iniciar a área de trabalho ")
    print("A área de trabalho foi invocada")
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    print("Main foi invocado como programa")
    print("-"*30)
    workspace()
else:
    print("Main foi invocado como módulo")
    print("-"*30)
    workspace()
