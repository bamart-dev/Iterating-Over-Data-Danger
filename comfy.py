from data import ONE_GROCERY, TWO_GROCERY

def comfy_zone():
    print("==COMFY ZONE==")
    
    # make copies so that we don't modify the original lists
    one_grocery = list(ONE_GROCERY)
    two_grocery = list(TWO_GROCERY)

    # appears to work
    one_grocery = filter_grocery_stores(one_grocery)

    # smooth sailin'
    two_grocery = filter_grocery_stores(two_grocery)

    print(f"{one_grocery=}")
    print(f"{two_grocery=}")

def filter_grocery_stores(stores):
    # rather than modifying the original list, create a
    # filtered copy by leaving out the stores we were
    # trying to remove.
    # actually more computationally efficient than using
    # either pop or remove from the other approaches
    
    filtered = []
    for store in stores:
        if store["type"] != "grocery":
            filtered.append(store)

    return filtered
            
    # the following python idiom makes this even more concise
    # (follow your curiosity)
    # filtered = [store for store in stores if store["type"] != "grocery"]
