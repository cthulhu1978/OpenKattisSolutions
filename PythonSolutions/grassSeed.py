def main():
    cost_of_seed = float(input())
    num_lawns = int(input())
    cost_total = 0
    for x in range(num_lawns):
        l,w = map(float, input().split())
        cost_total += (l * w) * cost_of_seed
    print(cost_total)





if __name__ == '__main__':
    main()
