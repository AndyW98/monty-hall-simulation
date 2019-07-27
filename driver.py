from host import Host
from player import Player
from manager import Manager

def main():
    player = Player('sucker')
    manager = Manager()
    print(manager.no_money(1))
    manager.list_doors()

if __name__ == "__main__":
    main()