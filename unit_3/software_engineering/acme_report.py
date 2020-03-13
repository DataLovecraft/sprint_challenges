#!/usr/bin/env python

'''
Utility functions to make and report data on Acme products.
'''
from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Rocket']


def generate_products(num_products=30):
    '''
    Generates random Acme products
    '''
    products = []
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                                flammability=flammability))
    return products

#    Alternative method:
#    To DO:
#    products
#    for _ in range(num_products):
#        name = random.choice(ADJECTIVES) + ' ' + rondom.choice(NOUNS)
#        weight = random.choice(weight)
#        flammability = random.choice(flammability)
#        gen_list.append(get_flamm_rand())
#        products.append(naem, price=price, weight-weight, flammability=flammability)
#    return products

def inventory_report(products):
    '''
    Takes a list of products and prints out a summary
    '''
    names = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0.0
    for product in products:
        names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: {}".format(len(names)))
    print("Average price: {}".format(total_price / len(products)))
    print("Average weight: {}".format(total_weight / len(products)))
    print("Average flammability: {}".format(
        total_flammability / len(products)))


if __name__ == '__main__':
    inventory_report(generate_products())
