def diagonal_list(num):
        '''
    (int) -> none
    prints a square of given number with a rhobush space

    diagonal_string(5)
    >>>
    5432112345
    5432  2345
    543    345
    54      45
    5        5
    54      45
    543    345
    5432  2345
    5432112345

    diagonal_strings(10)
    >>>
    0198765432112345678910
    0198765432  2345678910
    019876543    345678910
    01987654      45678910
    0198765        5678910
    019876          678910
    01987            78910
    0198              8910
    019                910
    01                  10
    0                    0
    01                  10
    019                910
    0198              8910
    01987            78910
    019876          678910
    0198765        5678910
    01987654      45678910
    019876543    345678910
    0198765432  2345678910
    0198765432112345678910


    '''
    number_list = list(range(1,num+1))
    list_num = number_list[::-1]+number_list[1:]


    print("".join((map(str,list_num))))
    for row in range(len(list_num)//2):
        list_num[len(list_num)//2-(row)] = " "
        list_num[len(list_num)//2+(row)] = " "
        print("".join((map(str,list_num))))

    for row in range(len(list_num)//2+1,len(list_num)):
        list_num[row-len(list_num)//2] = len(list_num)-(row)
        list_num[-((row-(len(list_num)//2))+1)] = len(list_num)-(row)
        print("".join((map(str,list_num))))

# def diagonal_string(num):
#     number_set = ""
#     for i in range(1,num+1):
#         number_set = number_set +str(i)
#     reverse_number_set = number_set[::-1]
#     string_sequence = reverse_number_set+number_set[1:]
#     for row in range(num):
#         print (reverse_number_set[:(num)-row]+" "*2*row + number_set[(row):])

#     for row in range(num+1,(2*num+1)):
#         print (reverse_number_set[:(row-num)]+" "*(2*(2*num-row)+1) + number_set[(num-row):])

def diagonal_strings(num):
    '''
    (int) -> none
    prints a square of given number with a rhobush space

    diagonal_string(5)
    >>>
    5432112345
    5432  2345
    543    345
    54      45
    5        5
    54      45
    543    345
    5432  2345
    5432112345

    diagonal_strings(10)
    0198765432112345678910
    0198765432  2345678910
    019876543    345678910
    01987654      45678910
    0198765        5678910
    019876          678910
    01987            78910
    0198              8910
    019                910
    01                  10
    0                    0
    01                  10
    019                910
    0198              8910
    01987            78910
    019876          678910
    0198765        5678910
    01987654      45678910
    019876543    345678910
    0198765432  2345678910
    0198765432112345678910


    '''
    number_set = ""
    for i in range(1,num+1):
        number_set = number_set +str(i)
    reverse_number_set = number_set[::-1]
    string_sequence = reverse_number_set+number_set[1:]
    for row in range(len(string_sequence)//2):
        print (reverse_number_set[:len(reverse_number_set)-row]+" "*2*row + number_set[(row):])

    for row in range(len(string_sequence)//2+1,len(string_sequence)+1):
        print (reverse_number_set[:(row-len(string_sequence)//2)]+" "*2*((len(string_sequence)-row)) + number_set[len(string_sequence)//2-row:])



if __name__ == '__main__':

    num = int(input("Enter a number\n>>> "))
    #diagonal_list(num)

    diagonal_strings(num)
