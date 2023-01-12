shop = [['футболка', 800], ['кроссовки', 5000], ['штаны', 500], ['шорты', 960], ['штаны', 450], ['кепка', 600], ['куртка', 9000], ['кроссовки', 2000], ['штаны', 870]]
commodity = input()

sum = 0
count = 0
for i in shop:
    if i[0] == commodity:
        count += 1
        sum+= i[1]

print(commodity,"count " + str(count),"sum "+ str(sum))
