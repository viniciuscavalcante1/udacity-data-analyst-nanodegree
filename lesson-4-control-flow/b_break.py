def screen_split(screen_number=80):
    print('-' * screen_number)


print("Break and continue manifest:")
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    if weight >= 100:
        break
    elif weight + cargo_weight > 100:
        continue
    else:

        items.append(cargo_name)
        weight += cargo_weight
print(items)
print(weight)


screen_split()
print("Break the String")

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)