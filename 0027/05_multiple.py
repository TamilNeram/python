#!/usr/bin/python3
#அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்,பிரி=" ",முடி='\n',கோப்பு=None,பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி,end=முடி, file=கோப்பு,flush=பறிப்பு)
    
# உள்ளீடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.    
def உள்ளீடு(*வாதங்கள்):
    அ = input (*வாதங்கள்)
    return அ

from tkinter import *
from tkinter import ttk        
    
வேர் = Tk()

label1 = ttk.Label(வேர், text = 'Label 1')
label2 = ttk.Label(வேர், text = 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<BP> Label'))
label1.bind('<1>', lambda e: print('<1> Label'))

வேர்.bind('<1>', lambda e: print('<1> வேர்'))

label1.unbind('<1>')
label1.unbind('<ButtonPress>')

வேர்.bind_all('<Escape>', lambda e: print('Escape!'))

வேர்.mainloop()
