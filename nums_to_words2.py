
#                                                                         .
# TBD: words to numbers?

ZERO =        'zero'

ONES =   { 0: '',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           None: ''}
            
TEENS =  {10: 'ten',
          11: 'eleven',
          12: 'twelve',
          13: 'thirteen',
          14: 'fourteen',
          15: 'fifteen',
          16: 'sixteen',
          17: 'seventeen',
          18: 'eighteen',
          19: 'nineteen',
          None: ''}

TENS =   { 0: '',
           #1: '', teens 
           2: 'twenty',
           3: 'thirty',
           4: 'fourty',
           5: 'fifty',
           6: 'sixty',
           7: 'seventy',
           8: 'eighty',
           9: 'ninety',
           None: ''}

# grouped by thousands, starting with hundred at 0. 
# Made to start with hundred for customization; 
# ie. diff language, country, etc
GROUPS = ['hundred',
          'thousand',
          'million',
          'billion',
          'trillion',
          'quadrillion',
          'quintillion',]

def digitalize(group):
    'splits group into hunds, tens, ones digits'
    if len(group) == 3:
        hunds = group[-3]
        tens  = group[-2]
        ones  = group[-1]
    elif len(group) == 2:
        hunds = None
        tens  = group[-2]
        ones  = group[-1]
    else:
        hunds = None
        tens  = None
        ones  = group[-1]
    return hunds, tens, ones

def name_digits(group, ONES, TEENS, TENS):
    'splits num to hunds, tens, ones digits and names them'
    teens = group[-2:]
    teens = TEENS.get(int(teens), '')
    group = list(map(int, group))
    hunds, tens, ones = digitalize(group)
    hunds = ONES[hunds]
    tens  = TENS[tens] if not teens else teens
    ones  = ONES[ones] if not teens else ''
    return [hunds, tens, ones]

def insert_hundreds(group, hunds_name):
    'inserts hundreds name between already named digits in group'
    hunds = group[0]
    if hunds: group.insert(1, hunds_name)
    return group

def name_group(group, group_name, GROUPS):
    'names the whole group, i.e thousand, million, etc'
    group = insert_hundreds(group, GROUPS[0])
    if group_name and any(group): 
        group.append(GROUPS[group_name])
    return group

def to_words(num, *, ZERO=ZERO, ONES=ONES, TEENS=TEENS, TENS=TENS, 
                     GROUPS=GROUPS, NEGATIVE='negative'):
    num   = int(num)
    neg   = num < 0
    num   = str(num)[1:] if neg else str(num)
    words = []
    group_name = 0 # index to GROUPS names mapper
    # start loop
    if int(num) == 0: return [ZERO]
    while num:
        group = num[-3:]
        group = name_digits(group, ONES, TEENS, TENS)
        group = name_group(group, group_name, GROUPS)
        words = group + words
        num   = num[:-3]
        group_name += 1
    # end loop
    else:
        if neg: words = [NEGATIVE] + words
    return words

if __name__ == '__main__':
    while True: 
        words = to_words(input('enter an integer: '))
        words = ' '.join(words)
        words = words.split()
        words = ' '.join(words)
        print(words)
