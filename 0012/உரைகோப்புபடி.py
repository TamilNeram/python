#!/usr/bin/env python3
# அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள், பிரி=" ", முடி='\n', கோப்பு=None, பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி, end=முடி, file=கோப்பு, flush=பறிப்பு)

# உள்ளீடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.


def உள்ளீடு(*வாதங்கள்):
    அ = input(*வாதங்கள்)
    return அ


def முதன்மை():
    கோ = open('உரைகோப்பு.உரை')
    for வரி in கோ:
        print(வரி.rstrip())


if __name__ == '__main__':
    முதன்மை()
