def get_num_words(book:str) -> int:
    num_words = len(book.split())
    return num_words


def get_num_characters(book:str) -> dict[str:int]:
    char_dict:dict[str:int] = {}
    characters:str = ''.join(book.split())
    for i in range(len(characters)):
        if characters[i].lower() in char_dict:
            char_dict[characters[i].lower()] += 1
        else:
            char_dict[characters[i].lower()] = 1

    return char_dict

def get_book_report(book:str):
    lis_tups = get_num_characters(book).items()
    sorted_lis = sorted(lis_tups, reverse=True, key=lambda item: item[1])
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {get_num_words(book)} total words')    
    print('--------- Character Count -------')
    for i in range(len(sorted_lis)):
        print(f'{sorted_lis[i][0]}: {sorted_lis[i][1]}')
    print('============= END ===============')
    return None

