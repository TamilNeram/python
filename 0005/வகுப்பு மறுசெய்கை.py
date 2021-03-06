#!/usr/bin/env python3

#அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்,பிரி=" ",முடி='\n',கோப்பு=None,பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி,end=முடி, file=கோப்பு,flush=பறிப்பு)
    
# உள்ளீடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.    
def உள்ளீடு(*வாதங்கள்):
    அ = input (*வாதங்கள்)
    return அ

class வரம்பு:
    def __init__(சுயம், *வாதங்கள்):
        வாதஎண்ணிகை = len(வாதங்கள்)
        சுயம்._தொடங்கு = 0
        சுயம்._படி = 1
        
        if வாதஎண்ணிகை < 1:
            raise TypeError(f'குறைந்தது 1 வாதம் எதிர்பார்க்கப்படுகிறது, கிடைத்தது {வாதஎண்ணிகை}')
        elif வாதஎண்ணிகை == 1:
            சுயம்._நிறுத்து = வாதங்கள்[0]
        elif வாதஎண்ணிகை == 2:
            (சுயம்._தொடங்கு, சுயம்._நிறுத்து) = வாதங்கள்
        elif வாதஎண்ணிகை == 3:
            (சுயம்._தொடங்கு, சுயம்._நிறுத்து, சுயம்._படி) = வாதங்கள்
        else: raise TypeError(f'அதிகபட்சம் 3 வாதங்கள் எதிர்பார்க்கப்படுகிறது, கிடைத்தது {வாதஎண்ணிகை}')

        சுயம்._அடுத்தது = சுயம்._தொடங்கு
    
    def __iter__(சுயம்):
        return சுயம்

    def __next__(சுயம்):
        if சுயம்._அடுத்தது > சுயம்._நிறுத்து:
            raise StopIteration
        else:
            _ர = சுயம்._அடுத்தது
            சுயம்._அடுத்தது += சுயம்._படி
            return _ர

def முதன்மை():
    for ந in வரம்பு(25):
        அச்சிடு(ந, முடி=' ')
    அச்சிடு()

if __name__ == '__main__': முதன்மை()
