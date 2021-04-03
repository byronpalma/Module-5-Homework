if __name__ == "__main__":
# creating and adding to a list
    food = ['rice', 'beans']
    print(food)

    food.append('broccoli')
    print(food)

    more_food = ['bread', 'pizza']
    food.extend(more_food)
    print(food)

# using slicing and index notation

    print(f'first two items: {food[0:2]}')
    print(f'last item: {food[4]}')
# creating a list
    breakfast = "eggs fruit orangejuice".split()
    print(breakfast)
    print(len(breakfast))

