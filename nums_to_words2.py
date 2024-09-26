
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

def to_words(num, *, ZERO=ZERO, ONES=ONES, TEENS=TEENS, TENS=TENS, 
                     GROUPS=GROUPS, NEGATIVE='negative'):
    num   = int(num)
    neg   = num < 0
    num   = abs(num)
    if num == 0: return [ZERO]
    num   = str(num)
    words = []
    group_num = 0
    # start loop
    while num:
        group = num[-3:]
        teens = group[-2:]
        teens = TEENS.get(int(teens), '')
        group = list(map(int, group))
        hunds, tens, ones = digitalize(group)
        hunds = ONES[hunds]
        tens  = TENS[tens] if not teens else teens
        ones  = ONES[ones] if not teens else ''
        group = [hunds, tens, ones]
        if hunds: 
            group.insert(1, GROUPS[0])
        if group_num and any([hunds, tens, ones]): 
            group.append(GROUPS[group_num])
        words = group + words
        num   = num[:-3]
        group_num += 1
    # end loop
    else:
        if neg: words = [NEGATIVE] + words
    return words
while True: 
    words = to_words(input('enter an integer: '))
    words = ' '.join(words)
    words = words.split()
    words = ' '.join(words)
    print(words)
