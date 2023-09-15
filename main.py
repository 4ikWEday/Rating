import time as t
serials_db = [ { "title": "Chronicles of the Galaxy", "genre": "Adventure", "seasons": 5, "rating": 8 }, { "title": "Mystery Island", "genre": "Fantasy", "seasons": 3, "rating": 9 }, { "title": "Epic Quest", "genre": "Fantasy", "seasons": 4, "rating": 7 }, { "title": "Crime Files", "genre": "Crime Drama", "seasons": 6, "rating": 5}, { "title": "Medical Miracles", "genre": "Medical Drama", "seasons": 2, "rating": 8 }, { "title": "Time Travelers", "genre": "Adventure", "seasons": 4, "rating": 8 }, { "title": "Comedy Central", "genre": "Comedy", "seasons": 7, "rating": 9 } ]

def search_by_genre(search_genre):
    genre_list = []
    for i in serials_db:
        if i['genre'] == search_genre:
            genre_list.append(i['title'])
    return genre_list


def search_by_rating(search_rating):
    rating_list = []
    for i in serials_db:
        if i['rating'] == search_rating:
            rating_list.append(i['title'])
    return rating_list


def print_info_about_all_shows():
    counter = 0
    for i in serials_db:
        if counter == 0:
            print()
        else:
            print('\n     *     *     *\n')
        print(f'TITLE: {i["title"]}')
        print(f'GENRE: {i["genre"]}')
        print(f'SEASONS: {i["seasons"]}')
        print(f'RATING: {i["rating"]}')
        t.sleep(2)
        counter += 1


def start():
    is_exit = False
    while not is_exit:
        print('1. Search TV shows by genre\n2. Search TV shows by rating\n3. Display information about all TV shows\n4. Exit')
        try:
            choice = int(input('Enter a number from 1 to 4:\n'))
        except:
            print('Input error. Try again!')
            return
        if choice == 1:
            genre_choice = input('Enter a genre:\n')
            genre_list = search_by_genre(genre_choice)
            if len(genre_list) == 0:
                print('No result. :C')
                return
            else:
                print()
                for i in genre_list:
                    print(i)
                print()
                t.sleep(3)
        if choice == 2:
            try:
                rating_choice = int(input('Enter a rating:\n'))
            except:
                print('Input error. Try again!')
                return
            rating_list = search_by_rating(rating_choice)
            if len(rating_list) == 0:
                print('No result. :C')
                return
            else:
                print()
                for i in rating_list:
                    print(i)
                print()
                t.sleep(3)
        if choice == 3:
            print('Information about all TV shows:')
            print_info_about_all_shows()
        if choice == 4:
            print('Exit...')
            is_exit = True

if __name__ == '__main__':
    start()
