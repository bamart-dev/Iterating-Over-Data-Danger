from danger import danger_zone
from safeish import safeish_zone
from safer import safer_zone
from comfy import comfy_zone

def main():
    danger_zone()  # avoid modifying while iterating
    # safeish_zone()  # safely modifies while iterating, but a little finicky
    # safer_zone()  # safely modifies, but makes a copy and is a little sneaky
    # comfy_zone()  # makes a copy for the result, but tends to be the preferred python approach

if __name__ == "__main__":
    main()