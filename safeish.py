from data import ONE_GROCERY, TWO_GROCERY

def safeish_zone():
    print("==SAFEISH ZONE==")
    
    # make copies so that we don't modify the original lists
    one_grocery = list(ONE_GROCERY)
    two_grocery = list(TWO_GROCERY)

    # appears to work
    remove_grocery_stores_inplace_SAFEISH(one_grocery)

    # looks good!
    remove_grocery_stores_inplace_SAFEISH(two_grocery)

    print(f"{one_grocery=}")
    print(f"{two_grocery=}")

def remove_grocery_stores_inplace_SAFEISH(stores):
    # avoids the iterator problem entirely by
    # writing a manual while loop.
    # works, but kind of clunky and easy to get wrong

    i = 0
    while i < len(stores):
        store = stores[i]
        if store["type"] == "grocery":
            stores.pop(i)
        else:
            i += 1

