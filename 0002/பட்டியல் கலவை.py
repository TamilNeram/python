#!/usr/bin/env python3
# அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்,பிரி=" ",முடி='\n',கோப்பு=None,பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி,end=முடி, file=கோப்பு,flush=பறிப்பு)

# உலகளாவிய மாறிகள் 
பிழைத்திருத்தநிலை = 0 # கூடு நிலை நிர்வகிக்கவும் 

def முதன்மை():
    வரம்பு = range(11)
    பட்டியல் = [ 1, 'இரண்டு', 3, {'4': 'நான்கு' }, 5 ]
    டூப்பிள் = ( 'ஒன்று', 'இரண்டு', None, 'நான்கு', 'ஐந்து' )
    தொகுப்பு = set("It's a bird! It's a plane! It's Superman!")
    அகராதி = dict( ஒன்று = வரம்பு, இரண்டு = பட்டியல், மூன்று = தொகுப்பு )
    கலவை = [ பட்டியல், வரம்பு, தொகுப்பு, அகராதி, டூப்பிள் ]
    காட்சி (கலவை)

def காட்சி (பொருள் ):
    global பிழைத்திருத்தநிலை 

    பிழைத்திருத்தநிலை  += 1
    if   isinstance(பொருள் , list):  அச்சிடு_படியல்(பொருள் )
    elif isinstance(பொருள் , range): அச்சிடு_படியல்(பொருள் )
    elif isinstance(பொருள் , tuple): அச்சிடு_tuple(பொருள் )
    elif isinstance(பொருள் , set):   அச்சிடு_set(பொருள் )
    elif isinstance(பொருள் , dict):  அச்சிடு_dict(பொருள் )
    elif பொருள்  is None: அச்சிடு('Nada', முடி=' ', பறிப்பு=True)
    else: அச்சிடு(repr(பொருள் ), முடி=' ', பறிப்பு=True)
    பிழைத்திருத்தநிலை  -= 1

    if பிழைத்திருத்தநிலை  <= 1: அச்சிடு() # வெளிப்புறத்திற்குப் பிறகு புதிய வரி 

def அச்சிடு_படியல்(பொருள் ):
    அச்சிடு('[', முடி=' ')
    for ஐ in பொருள் : காட்சி(ஐ)
    அச்சிடு(']', முடி=' ', பறிப்பு=True)

def அச்சிடு_tuple(பொருள் ):
    அச்சிடு('(', முடி=' ')
    for ஐ in பொருள் : காட்சி(ஐ)
    அச்சிடு(')', முடி=' ', பறிப்பு=True)

def அச்சிடு_set(பொருள் ):
    அச்சிடு('{', முடி=' ')
    for ஐ in sorted(பொருள் ): காட்சி(ஐ)
    அச்சிடு('}', முடி=' ', பறிப்பு=True)

def அச்சிடு_dict(பொருள் ):
    அச்சிடு('{', முடி=' ')
    for க, வி in பொருள்.items():
        அச்சிடு(க, முடி=': ' )
        காட்சி(வி)
    அச்சிடு('}', முடி=' ', பறிப்பு=True)

if __name__ == '__main__': முதன்மை()
