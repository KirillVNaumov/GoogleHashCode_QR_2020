import math

# file = open("a_example.txt")
# file = open("b_read_on.txt")
file = open("c_incunabula.txt")
# file = open("d_tough_choices.txt")
# file = open("e_so_many_books.txt")
# file = open("f_libraries_of_the_world.txt")
# file = open("my_ex.txt")

list1st = list(map(int, file.readline().split()))
tot_books = list1st[0]
tot_lib = list1st[1]
tot_days = list1st[2]
books_scores = list(map(int, file.readline().split()))

# print ("Book scores: ", books_scores)

list_lib = []
index = 0
while True:
    line = file.readline()
    if not line:
        break
    new_elem = []
    new_elem = list(map(int, line.split()))
    line = file.readline()
    books_tmp = list(map(int, line.split()))
    books_tmp = list(set(books_tmp)) 
    books_tmp = sorted(books_tmp, key=lambda x: books_scores[x], reverse=True)
    new_elem.append(books_tmp)
    new_elem.append(index)
    list_lib.append(new_elem)
    index += 1

def books_score_until_end(lib, left_days):
    if left_days > days_on_onelib(lib):
        return book_score_onelib(lib)
    days_to_score = left_days - lib[1]
    if (days_to_score <= 0):
        return 0
    num_books = 0
    for _ in range(days_to_score):
        num_books += lib[2]
    if (num_books >= lib[0]):
        return book_score_onelib(lib)
    score = 0
    for i in range(num_books):
        score += books_scores[lib[3][i]]
    return score

def book_score_onelib(lib):
    score = 0
    for i in lib[3]:
        score += books_scores[i]
    return score
    
def days_on_onelib(lib):
    sign_up =lib[1]
    ship = lib[2]
    num_books = lib[0]
    days = sign_up + math.ceil(num_books / ship)
    return days

# for i in list_lib:score_until_end(i, tot_days))
    # print (days_on_onelib(i))
    # print(book_score_onelib(i))

for i in reversed(range(len(list_lib))):
    if (not books_score_until_end(list_lib[i], tot_days)):
        list_lib.pop(i)


list_lib = sorted(list_lib, key=lambda lib: books_score_until_end(lib, tot_days), reverse=True)
lib_result = []
while True:
    if (not len(list_lib)):
        break
    if (list_lib[0] == 0):
        break
    best_res = books_score_until_end(list_lib[0], tot_days)
    if (not best_res):
        break 
    list_of_best = []
    for i in list_lib:
        if (books_score_until_end(i, tot_days) != best_res):
            break
        list_of_best.append(i)
    if (len(list_of_best) > 1):
        list_of_best = sorted(list_of_best, key=lambda lib: lib[1])
    tot_days = tot_days - list_of_best[0][1]
    lib_result.append(list_of_best[0])
    for i in list_of_best[0][3]:
        books_scores[i] = 0
    list_lib.remove(list_of_best[0])
    for i in reversed(range(len(list_lib))):
        if (not books_score_until_end(list_lib[i], tot_days)):
            list_lib.pop(i)
    list_lib = sorted(list_lib, key=lambda lib: books_score_until_end(lib, tot_days), reverse=True)


print(len(lib_result))
for i in lib_result:
    print (i[4], i[0])
    for j in i[3]:
        print (j, "", end="")
    print ()