#
# செயல்பாடுகளுடன் பணியாற்றுவதற்கான எடுத்துக்காட்டு கோப்பு
#

# அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்):
    print(*வாதங்கள்)

# ஒரு அடிப்படை செயல்பாட்டை வரையறுக்கவும்
def செயல்பாடு1():
    அச்சிடு("நான் ஒரு செயல்பாடு")

# வாதங்களை எடுக்கும் செயல்பாடு
def செயல்பாடு2(வாதம்1,வாதம்2):
    அச்சிடு(வாதம்1," ",வாதம்2)

# ஒரு மதிப்பை வழங்கும் செயல்பாடு
def கனசதுரம்( நீளம் ):
    return  நீளம்*நீளம்*நீளம்

# ஒரு வாதத்திற்கான இயல்புநிலை மதிப்புடன் செயல்பாடு
def சக்தி (எண்,அ=1):
    பலன்=1
    for க in range(அ):
        பலன்=பலன்*எண்
    return பலன்

#மாறக்கூடிய வாதங்களுடன் செயல்பாடு
def பலசேர் (*வாதங்கள்):
    பலன்=0
    for க in வாதங்கள்:
        பலன் = பலன் + க
    return பலன்


செயல்பாடு1()
அச்சிடு (செயல்பாடு1())
அச்சிடு (செயல்பாடு1)
செயல்பாடு2(10,20)
அச்சிடு (செயல்பாடு2(30,40))
அச்சிடு (கனசதுரம்(10))
அச்சிடு (சக்தி(2))
அச்சிடு (சக்தி(2,3))
அச்சிடு (சக்தி (எண்=4,அ=3))
அச்சிடு (பலசேர்(1,2,3,4,5,6,7,8,9))

