from data import ONE_GROCERY, TWO_GROCERY

def danger_zone():
    print("==DANGER ZONE==")

    # make copies so that we don't modify the original lists
    one_grocery = list(ONE_GROCERY)
    two_grocery = list(TWO_GROCERY)

    # appears to work
    remove_grocery_stores_inplace_DANGER(one_grocery)

    # after running, there's still a grocery store?!
    remove_grocery_stores_inplace_DANGER(two_grocery)

    print(f"{one_grocery=}")
    print(f"{two_grocery=}")

def remove_grocery_stores_inplace_DANGER(stores):
    # here be dragons!
    # the dangers are discussed in the slide deck
    
    for store in stores:
        if store["type"] == "grocery":
            stores.remove(store)

