from data import ONE_GROCERY, TWO_GROCERY


def safer_zone():
    print("==SAFER ZONE==")

    # make copies so that we don't modify the original lists
    one_grocery = list(ONE_GROCERY)
    two_grocery = list(TWO_GROCERY)

    # appears to work
    remove_grocery_stores_inplace_SAFER(one_grocery)

    # looks good!
    remove_grocery_stores_inplace_SAFER(two_grocery)

    print(f"{one_grocery=}")
    print(f"{two_grocery=}")


def remove_grocery_stores_inplace_SAFER(stores):
    # note the extra list() call
    # this is actually iterating over a _copy_ of the
    # original list, and using that to find the items to
    # remove from the actual original list.
    # easy to overlook, and it's a little weird to iterate
    # over one list, using that to modify another,
    # but it gets the job done

    for store in list(stores):
        if store["type"] == "grocery":
            stores.remove(store)
