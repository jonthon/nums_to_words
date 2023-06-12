
#                                                                         .
# TBD: words to numbers?
BASE = 10

ONES =   { 0: 'zero',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine'}
            
TEENS =  {10: 'ten',
          11: 'eleven',
          12: 'twelve',
          13: 'thirteen',
          14: 'fourteen',
          15: 'fifteen',
          16: 'sixteen',
          17: 'seventeen',
          18: 'eighteen',
          19: 'nineteen'}

TENS =   { 2: 'twenty',
           3: 'thirty',
           4: 'fourty',
           5: 'fifty',
           6: 'sixty',
           7: 'seventy',
           8: 'eighty',
           9: 'ninety'}

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

class Num:
    # keywords for custom use
    # ie. diff language or country ...etc
    def __init__(self, num, *,
                 base=BASE, ones=ONES, tens=TENS,
                 teens=TEENS, groups=GROUPS, negative='negative'):
        self.num      = num
        self.base     = base
        self.ones     = ones
        self.tens     = tens
        self.teens    = teens
        self.groups   = groups
        self.negative = negative

    def to_words(self):
        if int(self.num) == 0: return self.ones[0]
        def pop(group):
            for _ in range(3):
                try:  yield (group.pop())
                except IndexError: yield (None)
        num = list(map(int, str(self.num)))
        GRP, WORDS  = 0, []
        while num:
            word,  words       = None, []
            group, num         = num[-3::], num[:-3:]
            ones,  tens, hunds = pop(group)
            if hunds: 
                word = self.ones[hunds]
                words.append(word)
                words.append(self.groups[0])
            if tens:
                if not (tens == 1): word = self.tens[tens] 
                else: word = self.teens[tens * self.base + ones]
                words.append(word) 
            if ones and not (tens == 1): 
                word = self.ones[ones]
                words.append(word)    
            if len(str(self.num)) > 3 and words and GRP: 
                words.append(self.groups[GRP])
            WORDS = words + WORDS
            GRP  += 1
        return WORDS

if __name__ == '__main__':
    while True:
        num  = int(input('enter number in decimal: '))
        print(Num(num).to_words())
    