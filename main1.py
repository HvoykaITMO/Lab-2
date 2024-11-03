import csv
from csv import DictReader
from timeit import repeat


author = input('Enter the author`s name: ')
output = open('text.txt', 'w')

with open('books-en.csv') as csvf:
    table = DictReader(csvf, delimiter=';', quotechar='"')
    title_len_over_30 = 0
    find_book = []
    k = 0
    publishers = set()
    most_popular = []
    with open('text.txt', 'w') as f:
        for row in table:
            most_popular.append((int(row['Downloads']), row['Book-Title']))
            publishers.add(row['Publisher'])
            if len(row['Book-Title']) > 30:
                title_len_over_30 += 1
            if row['Book-Author'] == author and int(row['Year-Of-Publication']) in [2014, 2016, 2017]:
                find_book.append([row['Book-Title'], row['Year-Of-Publication']])
            if k < 20:
                k += 1
                f.write(f'{k}) {row["Book-Author"]}. {row['Book-Title']} - {row['Year-Of-Publication']}\n')

    print('\n1) Название длиннее 30 символов:', title_len_over_30)

    print(f'\n2) Книги автора {author}:', end=' ')
    if len(find_book) == 0:
        print('Ничего не нашлось :( (В моём варианте нужно найти авторов 2014, 2016, 2017 годов, но таких в файле нет(')
    else:
        print(*[f'{find_book[0][0]} {find_book[0][1]} года'])
    print('\n3) Был сгенерирован файл с библиографическими ссылками.')
    print('\nДополнительно) Список всех издательсв без повторений:', end=' ' )
    print(*publishers, sep='; ')
    print('\nСамые популярные 20 книг:', end=' ')
    print(*map(lambda x: f'"{x[1]}"',sorted(most_popular, reverse=True)[:20]), sep=', ')

