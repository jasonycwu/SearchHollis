## Testing code to parse Japanese characters
from unidecode import unidecode
import json

test = "金融恐慌とユダヤ・キリスト教"
print(json.dumps(test))
encoded = test.encode('utf-16')



# strings = []
# with open("sampleJPNinput.txt", "r") as f:
#     for line in f:
#         for word in line:
#             print (unidecode(word))