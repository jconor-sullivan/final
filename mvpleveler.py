
Kindergarten_file = open("KindergartenList.txt", "r")
G1_file = open("G1List.txt", "r")
print("Welcome to the MVP Sentence Leveler. This MVP will inform you of whether an input word is the appropriate reading level for the intended audience. This program will be expanded upon to cover all grade levels. ")

k_data = Kindergarten_file.readlines()
g1_data = G1_file.readlines()

Kindergarten_file.close()
G1_file.close()

k_data_splitted = k_data[0].split(',')
g1_data_splitted = g1_data[0].split(',')

kindergarten_list = []
grade1_list = []

for elem in k_data_splitted:
    elem = elem.strip()
    elem = elem.strip('\'')
    kindergarten_list.append(elem)

for elem in g1_data_splitted:
    elem = elem.strip()
    elem = elem.strip('\'')
    grade1_list.append(elem)


while True:
    kindergarten_set = set(kindergarten_list)
    grade1_set = set(grade1_list + kindergarten_list)
    leveler = input("Please choose a grade: K or G1 >> ")
    if leveler == 'K':
        Kindergarten_input = input(
            "Please input word for Kindergarten leveling: ")
        if Kindergarten_input in kindergarten_set:
            print('This word is appropriate for a Kindergarten reading audience!')
        else:
            print(
                "I am sorry, this word is not appropriate for a Kindergarten reading audience.")
    elif leveler == 'G1':
        Grade1_input = input("Please input word for Grade 1 leveling: ")
        if Grade1_input in grade1_set:
            print('This word is appropriate for a Grade 1 reading audience!')
        else:
            print(
                'I am sorry, this word is not appropriate for a Grade 1 reading audience.')
    if input('Do you want to repeat? (y/n) ') == 'n':
        break
