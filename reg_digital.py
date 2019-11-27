#include: positive integer(0 not included) eg: 1 2 3 4
#([1-9][0-9]*)

#include:integer(0 include) 、decimal eg:-1   0     1   2   3   4
#(-?(0|([1-9][0-9]*)))

#include:integer(0 include) 、decimal eg:-1   0     1    0.2    2.3    2.01
#(-?((0|([1-9][0-9]*))(\.[0-9]*[1-9])?))  

#include:integer(0 include) 、decimal、percentage eg:-1   0  0.2/0.3    2.3    2/1  
#(-?((0|([1-9][0-9]*))(\.[0-9]*[1-9])?))(/(-?(0\.[0-9]*[1-9])|([1-9][0-9]*(\.[0-9]*[1-9])?)))?
#-----------------  sample following ------------------------------------
import re 
class RegDigital:
    '''this class  obtains regualar expression about digital'''
    @staticmethod
    def match_digital(inputed_str):
        '''this is a sample ,print the result you test

        inputed_str:the data you want to be test 
        '''

        pattern = r''   #replace your regular expression
        regex = re.compile(pattern)
        for i in regex.finditer(inputed_str):
            print(i.group())



if __name__ == "__main__":
    RegDigital.match_digital('''Hello World -12.6
                                Nihao  123
                                How are you  -12
                                1.24
                                asdk 34%,
                                precent 1/2
                                2003 - 2005
                                0
                                0.123
                                0123
                                123/-0.2313''')
