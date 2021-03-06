import re

PATTERN = r'@gmail.com'
pattern = re.compile('@gmail.com$')


def test(name):
    return re.search(PATTERN, name)


marksheet = [(input().split(' ')) for _ in range(int(input()))]

for entry in sorted(marksheet, key=lambda data: data[0]):
    '''
    sort complex objects using some of the objects indices as a key
    '''
    if test(entry[1]):
        print(entry[0])

'''
30
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
riya ariya@gmail.com
julia bjulia@julia.me
julia csjulia@gmail.com
julia djulia@gmail.com
samantha esamantha@gmail.com
tanya ftanya@gmail.com
riya riya@live.com
julia julia@live.com
julia sjulia@live.com
julia julia@live.com
samantha samantha@live.com
tanya tanya@live.com
riya ariya@live.com
julia bjulia@live.com
julia csjulia@live.com
julia djulia@live.com
samantha esamantha@live.com
tanya ftanya@live.com
riya gmail@riya.com
priya priya@gmail.com
preeti preeti@gmail.com
alice alice@alicegmail.com
alice alice@gmail.com
alice gmail.alice@gmail.com

output
alice
alice
julia
julia
julia
julia
preeti
priya
riya
riya
samantha
samantha
tanya
tanya
'''
