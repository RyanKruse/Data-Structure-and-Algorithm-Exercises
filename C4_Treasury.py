
def make_change(coin_list, coin_input, min_coins, coins_used):
    for cents in range(coin_input + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[coin_input]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


coin_list = [1, 5, 10, 25]
coin_input = 42
coin_count = [0]*(coin_input+1)
coins_used = [0]*(coin_input+1)
make_change(coin_list, coin_input, coin_count, coins_used)
print_coins(coins_used, coin_input)
# TODO: Clean up this code yo.


def treasury(v, wt, n, W):
    """
    :param v: Values list
    :param wt: Weights list
    :param n: Number of distinct items
    :param W: Bag weight capacity (integer)
    :return: Returns combo.
    """
    k = []
    for _ in range(0, n + 1):
        temp = []
        for _ in range(0, W + 1):
            temp.append(0)
        k.append(temp)

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i - 1] <= w:
                k[i][w] = max(v[i - 1] + k[i-1][w-wt[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]

    print(k)
    return k[n][W]


# TODO: I have legit no idea how this algorithm works. Walk it through step by step with self.
values = [3, 4, 8, 8, 10]
weights = [2, 3, 4, 5, 9]
number = len(values)
W = 10
ans = treasury(values, weights, number, W)
print(str(ans) + '\n\n')


class Treasury:
    def __init__(self, items, carry_limit):
        self.items = items
        self.raw_carry_limit = carry_limit
        self.carry_limit = carry_limit
        self.weight_count = [0] * (carry_limit + 1)
        self.max_value = [0] * (carry_limit + 1)
        self.nells_bag = []

    def plot(self):
        for weight in range(self.raw_carry_limit + 1):
            weight_count = weight
            new_item = [1, 2]
            for item in [c for c in self.items if c[0] <= weight]:
                b1 = self.max_value[weight - item[0]] + 1
                b2 = weight_count
                if b1 < b2:
                    weight_count = b1
                    new_item = item
            self.max_value[weight] = weight_count
            self.weight_count[weight] = new_item

    def print_answer(self):
        print(self.nells_bag)
        print(self.weight_count)
        print(self.max_value)
        self.print_items()

    def print_items(self):
        weight = self.raw_carry_limit
        items_used = []
        while weight > 0:
            try:
                this_item = self.weight_count[weight]
            except IndexError:
                break
            if this_item in items_used:
                try:
                    weight += 1
                except IndexError:
                    weight -= 1
            else:
                items_used.append(this_item)
                weight = weight - this_item[0]

        total_weight = 0
        for item in items_used:
            total_weight += item[0]
        if total_weight > self.raw_carry_limit:
            # Nell throws spaghetti!
            smallest = [99, 99]
            for item in items_used:
                if item[0] < smallest[0]:
                    smallest = item
            if total_weight - smallest[0] <= self.raw_carry_limit:
                items_used.remove(smallest)
            else:
                smallest2 = [99, 99]
                for item in items_used:
                    if item[0] < smallest2[0] and item != smallest:
                        smallest2 = item
                if total_weight - smallest2[0] <= self.raw_carry_limit:
                    items_used.remove(smallest2)
                else:
                    print('This needs to be programmed into a recursive loop yo.')
        value_counter = 0
        weight_counter = 0
        for item in items_used:
            print(item)
            value_counter += item[1]
            weight_counter += item[0]
        print(f'Final Weight: {weight_counter} and Final Value: {value_counter}')


items = [[2, 3], [3, 4], [4, 8], [5, 8], [9, 10]]
treasury = Treasury(items, 20)
treasury.plot()
treasury.print_answer()
