# Module for unwrapping the Twitter friends of @POTUS from the json file returned
# by the Twitter Developer API

import json
from pprint import pprint

FILENAME = "POTUS-friends.json"


def unwrap_twitter_json(filename):
    print("\nUnwrapping {}\n\nAvailable commands: [print], [back], [quit]\n".format(filename))
    block_stack = []
    json_file = open(filename, encoding="utf-8")
    json_data = json.load(json_file)
    # pprint(json_data)
    innermost_block = json_data
    # block_stack.append(innermost_block)
    while True:
        if any([isinstance(innermost_block, type_) for type_ in (str, int, float)]):
            print(innermost_block)
        elif any([isinstance(innermost_block, type_) for type_ in (dict, list, tuple)]):
            if isinstance(innermost_block, dict):
                print("This block is a dictionary. Choose between these keys:",
                      innermost_block.keys())
            elif isinstance(innermost_block, list) or isinstance(innermost_block, tuple):
                print("This block is a list. Choose an index from 0 to",
                      len(innermost_block) - 1)
        else:
            print("This block is of", type(innermost_block),
                  "type. I'm not sure what to do with this one!")

        input_ = input("Which one? - ")
        if input_ == "[print]":
            print("CURRENT BLOCK:", innermost_block)
        elif input_ == "[quit]":
            print("QUITTING...")
            break
        elif input_ == "[back]":
            try:
                innermost_block = block_stack.pop()
            except IndexError:
                print("No way back!")
        else:
            try:
                index = int(input_) if isinstance(innermost_block, list) or \
                                       isinstance(innermost_block, tuple) else input_
                block_stack.append(innermost_block)
                innermost_block = innermost_block[index]
            except (KeyError, IndexError):
                print("No such key!")


if __name__ == "__main__":
    unwrap_twitter_json(FILENAME)
