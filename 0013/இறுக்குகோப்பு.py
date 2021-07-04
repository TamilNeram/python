# அச்சிடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.
import zipfile as இறுக்குகோப்பு


def அச்சிடு(*வாதங்கள், பிரி=" ", முடி='\n', கோப்பு=None, பறிப்பு=False):
    print(*வாதங்கள், sep=பிரி, end=முடி, file=கோப்பு, flush=பறிப்பு)

# உள்ளீடு வரையறு - பின் வரும் நிரல்களில் அச்சிடு பயன்படுத்தலாம்.


def உள்ளீடு(*வாதங்கள்):
    அ = input(*வாதங்கள்)
    return அ

# இறுக்குகோப்பு தொகுதி


# திறந்து பட்டியலிடுங்கள்
இறுக்கு = இறுக்குகோப்பு.ZipFile('காப்பகம்.இறுக்கு', 'r')
அச்சிடு(இறுக்கு.namelist())

# இறுக்கு கோப்புறையில் மெட்டாதரவு
for மெட்டா in இறுக்கு.infolist():
    அச்சிடு(மெட்டா)

#தகவல் = இறுக்கு.getinfo("வாங்கப்பட்டது.உரை")
தகவல் = இறுக்கு.getinfo("p.txt")
அச்சிடு(தகவல்)

# இறுக்கு கோப்புறையில் உள்ள கோப்புகளுக்கான அணுகல்
அச்சிடு(இறுக்கு.read("p.txt"))
with இறுக்கு.open('p.txt') as கோ:
    அச்சிடு(கோ.read())

# கோப்புகளை பிரித்தெடுக்கிறது
# இறுக்கு.extract("வாங்கப்பட்டது.உரை")
இறுக்கு.extractall()

# இறுக்கு கோப்பை மூடுவது
இறுக்கு.close()
