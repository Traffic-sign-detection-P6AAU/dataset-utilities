from data_handler.data_split import split_dataset
from data_handler.data_labeler import extend_annotations

CATEGORIES_PATH = 'data_handler/categories.json'

def main():
    print('---Menu list---')
    print('Type: 1 to split dataset')
    print('Type: 2 to extend the labels')
    choice = input()
    if choice == '1':
        split_dataset(CATEGORIES_PATH)
    elif choice == '2':
        extend_annotations()
    else:
        print('Input was not 1 or 2.')

if __name__ == '__main__':
    main()
