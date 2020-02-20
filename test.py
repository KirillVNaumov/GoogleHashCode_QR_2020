import math

def days_on_onelib(list_lib):
    sign_up =list_lib[1]
    ship = list_lib[2]
    num_books = list_lib[0]
    days = sign_up + math.ceil(num_books / ship)
    return days

file = open("a_example.txt")

list1st = list(map(int, file.readline().split()))
tot_books = list1st[0]
tot_lib = list1st[1]
tot_days = list1st[2]
books_scores = list(map(int, file.readline().split()))

print ("Book scores: ", books_scores)

list_lib = []

while True:
    line = file.readline()
    if not line:
        break
    new_elem = []
    new_elem = list(map(int, line.split()))
    line = file.readline()
    books_tmp = list(map(int, line.split()))
    books_tmp = sorted(books_tmp, key=lambda x: books_scores[x], reverse=True)
    new_elem.append(books_tmp)
    list_lib.append(new_elem)

for i in list_lib:
    print (days_on_onelib(i))