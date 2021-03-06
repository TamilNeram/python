#!/usr/bin/env python3

#அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்,பிரி=" ",முடி='\n',கோப்பு=None,பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி,end=முடி, file=கோப்பு,flush=பறிப்பு)
    
# உள்ளீடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.    
def உள்ளீடு(*வாதங்கள்):
    அ = input (*வாதங்கள்)
    return அ

import sys
import time as நேரம்

__version__ = '1.3.0'

class எண்சொற்கள்():
    '''
        எண்ணை சொற்களாகத் தரும்
        எ.கா., 42 --> 'நாற்பது-இரண்டு' ஆகிறது
    '''
    _சொற்கள் = {
        'ஒற்றைகள்': (
            'ஓ', 'ஒன்று', 'இரண்டு', 'மூன்று', 'நான்கு', 'ஐந்து', 'ஆறு', 'ஏழு', 'எட்டு', 'ஒன்பது'
        ), 'பத்துகள்': (
            '', 'பத்து', 'இருபது', 'முப்பது', 'நாற்பது', 'ஐம்பது', 'அறுபது', 'எழுபது', 'எண்பது', 'தொண்ணூறு'
        ), 'இருபதுகள்': (
            'பத்து', 'பதினொரு', 'பன்னிரண்டு', 'பதின்மூன்று', 'பதினான்கு', 'பதினைந்து', 'பதினாறு', 'பதினேழு', 'பதினெட்டு', 'பத்தொன்பது' 
        ), 'quarters': (
            'மணி', ' கால் ',' பாதி '
        ), 'வரம்பு': {
            'நூறு': 'நூறு'
        }, 'மற்றவை': {
            'கழித்தல்': 'கழித்தல்'
        }
    }
    _oor = 'வரம்பிற்கு வெளியே'    # வரம்பிற்கு வெளியே

    def __init__(சுய, n):
        சுய._எண் = n;

    def எண்சொற்கள்(சுய, num = None):
        'Return the எண் as சொற்கள்'
        n = சுய._எண் if num is None else num
        ச = ''
        if n < 0:           # negative  எண்கள் 
            ச += சுய._சொற்கள்['மற்றவை']['கழித்தல்'] + ' '
            n = abs(n)
        if n < 10:          # single-digit எண்கள்
            ச += சுய._சொற்கள்['ஒற்றைகள்'][n]  
        elif n < 20:        # இருபதுகள்
            ச += சுய._சொற்கள்['இருபதுகள்'][n - 10]
        elif n < 100:       # பத்துகள்
            m = n % 10
            t = n // 10
            ச += சுய._சொற்கள்['பத்துகள்'][t]
            if m: ச += '-' + எண்சொற்கள்(m).எண்சொற்கள்()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            ச += சுய._சொற்கள்['ஒற்றைகள்'][t] + ' ' + சுய._சொற்கள்['வரம்பு']['நூறு']
            if m: ச += ' ' + எண்சொற்கள்(m).எண்சொற்கள்()    # recurse for remainder
        else:
            ச += சுய._oor
        return ச

    def எண்(சுய, n = None):
        'setter/getter'
        if n is not None:
            சுய._எண் = n
        return str(சுய._எண்);

class நேரம்சொல்(எண்சொற்கள்):
    '''
        return the நேரம் (from two parameters) as சொற்கள்,
        எ.கா., மதியம் பதினான்கு , ஒன்று கடந்து கால், போன்றவை.
    '''

    _சிறப்புகள் = {
        'நண்பகல்': 'நண்பகல்',
        'நள்ளிரவு': 'நள்ளிரவு',
        'வரை': 'வரை',
        'கடந்து': 'கடந்து'
    }

    def __init__(சுய, h = None, m = None):
        சுய.நேரம்(h, m)

    def நேரம்(சுய, h = None, m = None):
        if h is not None:
            சுய._hour = abs(int(h))
        if m is not None:
            சுய._min = abs(int(m))
        return (h, m)

    def நேரம்_t(சுய, t = None):
        if t is None:
            t = நேரம்.localtime()
        சுய._hour = t.tm_hour
        சுய._min = t.tm_min

    def சொற்கள் (சுய):
        h = சுய._hour
        m = சுய._min
        
        if h > 23: return சுய._oor     # OOR errors
        if m > 59: return சுய._oor

        sign = சுய._சிறப்புகள்['கடந்து']        
        if சுய._min > 30:
            sign = சுய._சிறப்புகள்['வரை']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12

        # hword is the hours word)
        if h == 0: hword = சுய._சிறப்புகள்['நள்ளிரவு']
        elif h == 12: hword = சுய._சிறப்புகள்['நண்பகல்']
        else: hword = சுய.எண்சொற்கள்(h)

        if m == 0:
            if h in (0, 12): return hword   # for noon and midnight
            else: return "{} {}".format(சுய.எண்சொற்கள்(h), சுய._சொற்கள்['quarters'][m])
        if m % 15 == 0:
            return "{} {} {}".format(hword, sign,சுய._சொற்கள்['quarters'][m // 15] ) 
        return "{} {} {}".format(hword, sign, சுய.எண்சொற்கள்(m) ) 

    def digits(சுய):
        'return the traditionl நேரம், e.g., 13:42'
        return f'{சுய._hour:02}:{சுய._min:02}'

class நேரம்சொல்_t(நேரம்சொல்):   # wrapper for நேரம்சொல் to use நேரம் object
    '''
        set the நேரம் from a நேரம் object
    '''
    def __init__(சுய, t = None):
        சுய.நேரம்_t()

def முதன்மை():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            சோதனை()
        else:
            try: அச்சிடு(நேரம்சொல்(*(sys.argv[1].split(':'))).சொற்கள்())
            except TypeError: அச்சிடு('Invalid நேரம் ({})'.format(sys.argv[1]))
    else:
        அச்சிடு(நேரம்சொல்_t().சொற்கள்())

def சோதனை():
    நே = நேரம்சொல்()
    அச்சிடு('\nஎண்கள் சோதனை:')
    பட்டியல் = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30, 
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000 
    )
    for ஐ in பட்டியல்:
        நே.எண்(ஐ)
        அச்சிடு(ஐ, நே.எண்சொற்கள்())

    அச்சிடு('\nநேர சோதனை:')
    பட்டியல் = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for ஐ in பட்டியல்:
        நே.நேரம்(*ஐ)
        அச்சிடு(நே.digits(), நே.சொற்கள்())
    
    நே.நேரம்_t() # set நேரம் to now
    அச்சிடு('\nஉள்ளூர் நேரம் ' + நே.சொற்கள்())

if __name__ == '__main__': முதன்மை()
