import docx
import random

mydoc = docx.Document()

def print_hi(name):
    mydoc.save ("C:\\Users\\XXXXXXXXXXXXXX\\Desktop\\Liza.docx") # <----- Please change dest folder and name of .docx file
    print(f'File is .... {name}')  # print message if done

def calc_chr(): # method for randomly generate which math action will do
    calc_num = random.randint(0, 1)
    if calc_num == 0:
        calcul_char = '-'
    else:
        calcul_char = '+'
    return calcul_char

def rnd_num(): # method for randomly generate numbers for example
    number = random.randint(1, 99)
    return number

def calc_exemp (): # method for checking numbers and totals for example because my douter can calculate in range of 0 - 100
    number1 = rnd_num()
    number2 = rnd_num()
    calc_char = calc_chr()
    if calc_char == '-': # if minus than total must be not less than 0
        while number1 - number2 < 0:
            number1 = rnd_num()
            number2 = rnd_num()
    else: # if plus than total must be not more than 100
        while number1 + number2 > 100:
            number1 = rnd_num()
            number2 = rnd_num()
    exemp_str = str(str(number1) + str(calc_char) + str(number2) + ' = [                  ]')
    return exemp_str

if __name__ == '__main__':
    mydoc.add_paragraph('\t\t\t\t TIME: [                             ]')
    mydoc.save("C:\\Users\\XXXXXXXXXXXXXX\\Desktop\\Liza.docx") # <----- Please change dest folder and name of .docx file
    for i in range (1, 25): # in doc file will be generated 25 strings with 4 examples for each string
        calc_str1 = calc_exemp() # generate example 1
        calc_str2 = calc_exemp() # generate example 2
        calc_str3 = calc_exemp() # generate example 3
        calc_str4 = calc_exemp() # generate example 4
        calc_str = str(str(calc_str1) + '\t' + str(calc_str2) + '\t' + str(calc_str3) + '\t' + str(calc_str4)) # collect all examples in one string
        mydoc.add_paragraph(calc_str) # send string to doc
    print_hi('created!') # exit with message than done
