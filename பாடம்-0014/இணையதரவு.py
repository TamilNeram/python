# 
# இணையத்திலிருந்து தரவை மீட்டெடுப்பதற்கான எடுத்துக்காட்டு கோப்பு
# உலகளாவிய வள இருப்பிடம்->உவஇ->உவி = URL
#
import urllib.request as உவிநூலககோரிக்கை # பைதான் 2.7 இல் உள்ளதைப் போல urllib2 க்கு பதிலாக

def முதன்மை():
  # urllibஐப் பயன்படுத்தி "உலகளாவிய வள இருப்பிடம்->உவஇ->உவி" இணைப்பைத் திறக்கவும்
  உவிதரவு = "http://www.thirukkural.com/2009/01/blog-post_5472.html"
  #உவிதரவு = "http://tamilneram.github.io"
  # குறிப்பு https - பிழை ஏற்படுகிறது. SSL: CERTIFICATE_VERIFY_FAILED பிழை ஏற்பட்டால்,
  # பக்கத்தை பார் https://medium.com/@yen.hoang.1904/resolve-issue-ssl-certificate-verify-failed-when-trying-to-open-an-url-with-python-on-macos-46d868b44e10

  வலைஉவி = உவிநூலககோரிக்கை.urlopen(உவிதரவு)
  # குறிப்பு http - பிழை இல்லை.

  # முடிவு குறியீட்டைப் பெற்று அதை அச்சிடுங்கள்
  print ("முடிவு குறியீடு : " + str(வலைஉவி.getcode()))
  
  # உவியிலிருந்து தரவைப் படித்து அச்சிடுக
  தரவு8 = வலைஉவி.read() # பைட் கோவை 
  தரவு = தரவு8.decode("utf-8") # கோவையாக மாற்று
  
  #கோப்பில் எழுது
  கோப்பு = open('புகழ்-வலைதரவு.html','w+')
  கோப்பு.write(தரவு)
  கோப்பு.close()
  
if __name__ == "__main__":
  முதன்மை()
