#
# தேதி தகவலுடன் பணியாற்றுவதற்கான எடுத்துக்காட்டு கோப்பு
#

from datetime import date
from datetime import time
from datetime import datetime


def  முதன்மை ():
  ## தேதி பொருட்கள்
  # தேதி வகுப்பிலிருந்து எளிய இன்றைய () முறையிலிருந்து இன்றைய தேதியைப் பெறுங்கள்
  இன்று=date.today()
  print("இன்றைய தேதி : ", இன்று)

  # தேதியின் தனிப்பட்ட கூறுகளை அச்சிடுக
  print("தேதி கூறுகள்: ", இன்று.year, இன்று.month, இன்று.day)  

  
  # இன்றைய வாரநாளை மீட்டெடுக்கவும் (0 = திங்கள், 6 = ஞாயிறு)
  print ("இன்றைய வார நாள் எண்: ", இன்று.weekday())
  நாட்கள்= ["திங்கள்","செவ்வாய்","புதன்","வியாழன்","வெள்ளி","காரி","ஞாயிறு"]
  print ("இது ஒரு " + நாட்கள்[இன்று.weekday()]+" கிழமை")
    
  ## தேதிநேர பொருட்கள்
  # இன்றைய தேதியை தேதிநேர வகுப்பிலிருந்து பெறுங்கள்
  இன்று=datetime.now()
  print  ("தற்போதைய தேதி மற்றும் நேரம் ", இன்று)
  
  # தற்போதைய நேரத்தைப் பெறுங்கள்
  நேரம்=datetime.time(datetime.now())
  print ("தற்போதைய நேரம் ", நேரம்)

  
if __name__ == "__main__":
     முதன்மை();


  



  
