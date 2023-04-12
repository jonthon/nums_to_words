
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

    def digits(self):
        """
        returns number of digits and maximum value.
        """
        return len(str(self.num))

    def group_words(self):
        # string version could be a lot lot simpler
        digits      = self.digits()
        power       = self.base ** (digits - 1)
        num         = abs(self.num)
        group_words = []
        all_words   = []

        def traverse():                         # reuse
            nonlocal num, power, digits
            num    %= power
            power //= self.base
            digits -= 1

        def group_digit():                      # reuse
            return (digits % 3), (num // power)

        def new_group():                        # reuse
            nonlocal group_words
            all_words.append(group_words)
            group_words = []

        if not num: return [ONES[num]]
        while digits:                           
            group, digit = group_digit()

            # hundreds
            if group == 0 and digit:
                group_words.append(ONES[digit])
                group_words.append(GROUPS[0])         # repeating hundred => 0

            # tens
            elif group == 2 and digit:
                # twenty, thirty, forty, ...etc
                if   digit > 1: group_words.append(TENS[digit])
                # eleven, twelve, thirteen, ...etc
                elif digit == 1:
                    traverse()
                    group, digit = group_digit()
                    group_words.append(TEENS[self.base + digit])
                    new_group()

            # ones
            elif group == 1:
                if digit: group_words.append(ONES[digit])
                new_group()
            traverse()
            
        # append groups and save in instance namespace 
        all_words.reverse()
        for group, word in enumerate(all_words):
            if word:
                if group: word.append(self.groups[group])
            all_words[group] = ' '.join(word)
        all_words.reverse()
        return all_words

    def words(self):
        # customizable for other str processing
        # ie. adding commas, 'and', 'negative', etc.
        words = self.group_words()
        if self.num < 0: words.insert(0, self.negative)
        return ' '.join(filter(lambda i: bool(i), words))

class CustomNum(Num):
    def digits(self):
        digit = 0
        num   = abs(self.num)
        if not num: return 1, 1
        while num:
            digit += 1
            num  //= self.base
        return digit

   
if __name__ == '__main__':
    num  = int(input('enter number in decimal: '))
    print(Num(num).words())
    