def main():
    gold, silver, copper = map(int, input().split())
    buying_power = (gold * 3 + silver * 2 + copper)
    purchase_list = []

    province = Victory_card("Province",8, 6)
    duchy = Victory_card("Duchy", 5, 3)
    estate = Victory_card("Estate", 2, 1)

    gold = Treasure_card("Gold", 6, 3)
    silver = Treasure_card("Silver", 3, 2)
    copper = Treasure_card("Copper", 0, 1)

    Victory_card_list = [province, duchy, estate]
    Treasure_card_list = [gold, silver, copper]
    vic_card_buying = buying_power
    for i in Victory_card_list:
        if(i.get_cost() <= vic_card_buying):
            purchase_list.append(i.get_name())
            break


    for j in Treasure_card_list:
        if(j.get_cost() <= buying_power):
            purchase_list.append(j.get_name())
            break
    if len(purchase_list) > 1:
        print("{} or {}".format(purchase_list[0], purchase_list[1]))
    else:
        print("{}".format(purchase_list[0]))


class Victory_card():
    def __init__(self, name, cost, victory_points):
        self.name = name
        self.cost = cost
        self.victory_points = victory_points
    def get_cost(self):
        return self.cost
    def get_name(self):
        return self.name
    def get_vicpoints(self):
        return self.victory_points

class Treasure_card():
    def __init__(self, name, cost, buying_power):
        self.name = name
        self.cost = cost
        self.buying_power = buying_power
    def get_cost(self):
        return self.cost
    def get_name(self):
        return self.name



if __name__ == '__main__':
    main()
