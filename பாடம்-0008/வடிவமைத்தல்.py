#
# நேரம் மற்றும் தேதி வெளியீட்டை வடிவமைப்பதற்கான எடுத்துக்காட்டு கோப்பு.
#

# அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
def அச்சிடு(*வாதங்கள்):
    print(*வாதங்கள்)

from datetime import datetime

def முதன்மை():
  # நேரங்கள் மற்றும் தேதிகளை முன் வரையறுக்கப்பட்ட சரத்தின் தொகுப்பைப் பயன்படுத்தி வடிவமைக்க முடியும்
  # கட்டுப்பாட்டு குறியீடுகள்
  இப்போது = datetime.now () # தற்போதைய தேதி மற்றும் நேரத்தைப் பெறுங்கள்
  
  #### தேதி வடிவமைத்தல் ####
  
   #%y /%Y - ஆண்டு, %a/%A - வார நாள், %b/%B - மாதம், %d - மாத நாள்
  அச்சிடு (இப்போது.strftime ("நடப்பு ஆண்டு: %Y")) # நூற்றாண்டுடன் முழு ஆண்டு
  அச்சிடு (இப்போது.strftime ("%y-%B-%d-%a")) # சுருக்கமான ஆண்டு, முழு மாதம்,  நாள் எண்,  சுருக்கமான நாள்
  
   #%c - மொழியின் தேதி மற்றும் நேரம்,%x - மொழியின் தேதி,%X - மொழியின் நேரம்
  அச்சிடு (இப்போது.strftime ("மொழி தேதி மற்றும் நேரம்: %c"))
  அச்சிடு (இப்போது.strftime ("மொழி தேதி : %x"))
  அச்சிடு (இப்போது.strftime ("மொழி நேரம்: %X"))

   #### நேர வடிவமைப்பு ####
  
   #%I /%H - 12/24 மணி, %M - நிமிடம்,%S - வினாடி, % p - மொழியின் AM / PM 
  அச்சிடு (இப்போது.strftime ("தற்போதைய நேரம்: %I:%M:%S %p")) # 12-மணி:நிமிடம்:வினாடி:காலை
  அச்சிடு (இப்போது.strftime ("24-மணிநேர நேரம் : %H:%M")) # 24-மணி:நிமிடம்

         
if __name__ == "__main__":
  முதன்மை();
