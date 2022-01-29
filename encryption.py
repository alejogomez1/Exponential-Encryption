from key_code import Key_code
from message import Message

KEYS = {'#': '35', 'Q': '61', '0': '66', ' ': '88', 'W': '81', 'k': '46',
            '=': '75', 'E': '80', '+': '74', 'd': '20', '1': '43', 'z': '71',
            'F': '94', ';': '10', 'I': '47', 'U': '16', 'M': '09', 'e': '26',
            'n': '92', 'T': '56', 'B': '13', '7': '82', ')': '01', '4': '93',
            'Ñ': '76', 'Z': '07', 'i': '44', 'y': '14', 'P': '68', '/': '79',
            'o': '62', 'S': '58', '3': '34', '2': '30', 'p': '52', 'ú': '03',
            '¿': '70', 'ñ': '63', 'j': '73', 'L': '78', 'G': '04', 'a': '18',
            'q': '89', 'Y': '85', '*': '54', 'R': '60', 's': '67', "'": '65',
            'x': '83', 'N': '02', 'X': '32', 'ó': '49', 'V': '37', ']': '45',
            'r': '84', 'D': '53', 'v': '28', 'f': '06', '(': '29', 'J': '91',
            ':': '77', 'H': '19', '[': '33', 'l': '24', 'í': '59', '}': '41',
            'A': '64', '-': '72', 'O': '42', 'w': '36', '9': '40', 'g': '08',
            'b': '57', 'é': '23', '¡': '51', '?': '25', 'c': '38', '5': '12',
            'á': '27', '&': '15', '\n': '55', '8': '00', 'K': '21', '{': '69',
            '~': '48', 'C': '87', 'm': '22', 'h': '05', 'u': '11', 't': '31',
            '"': '90', '$': '50', '>': '97', '<': '96', '!': '86', '.': '95',
            '6': '17', ',': '98'}

class Encryption:
    message = Message('')
    key_code = Key_code()
    
    def __init__(self, message, key_code) -> None:
        self.message = message
        self.key_code = key_code

    def encrypt_message():
        pass

    def decipher_message():
        pass

    def __str_to_int(self):
        lenght = len(str(self.key_code.p))
        max = (lenght - 1)//2
        character_list = self.message.text
        integer_list = []
        count = 0
        group = '49'
        for index in range(len(character_list)):
            count += 1
            if count % max == 0:
                integer_list.append(group)
                group = KEYS[character_list[index]]
            else:
                group += KEYS[character_list[index]]
        integer_list.append(group)
        while len(integer_list[-1]) < 2 * max:
            integer_list += '49'
        return integer_list

    def __int_to_str(self):
        pass            
