# நேர தொகுதி மூலம் கண்காணிப்பை உருவாக்கவும் 

#அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்,பிரி=" ",முடி='\n',கோப்பு=None,பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி,end=முடி, file=கோப்பு,flush=பறிப்பு)
    
# உள்ளீடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.    
def உள்ளீடு(*வாதங்கள்):
    அ = input (*வாதங்கள்)
    return அ

import time as நேரம்

இயக்கு = உள்ளீடு ("தொடங்கு?>")

வினாடிகள்  = 0

if இயக்கு != "இல்லை":
    while வினாடிகள்  != 10:
        அச்சிடு (">", வினாடிகள் )
        நேரம்.sleep(1)
        வினாடிகள்  += 1
    அச்சிடு (">", வினாடிகள் )
