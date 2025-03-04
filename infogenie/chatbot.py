from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from PIL import Image
#from chatterbot.storage import StorageAdapter

import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>INFO GENIE</b>')

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "<b>Are you a Hosteller??<br>y Yes<br>n No</b>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///db.sqlite3'   
) 
trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
 "<b>Are you a Hosteller?<br>y Yes<br>n No</b>",
 "y",
"<b>f Fee <br>h Hostel Details <br>d Department Contacts</b>",
"f",
"<b>m Merit Seat <br>t Management Seat<br>o OEC<br>w Fee Waiver",
"m",
"<b> Merit Seat <br><br>Fee : 43150 <br>Fee already paid to Entrance Commissioner : 10000 <br> →Fee to be paid at Director’s Account :33150<br>Examination Fee:7730<br>Miscellaneous Fee : 9800<br>Hostel Fee:9250<br> →Total : (33150+7730+9800+9250) = 59930<br></b><b><br><br><b>Type ‘start’ to go back to main menu</b>",

"t",
"<b>Management Seat<br>Fee : 73150<br>Fee already paid to Entrance Commissioner : 10000 <br> →Fee to be paid at Director’s Account :63150<br>Examination Fee:7730<br>Miscellaneous Fee : 9800<br>Hostel Fee:9250<br> →Total :(63150+7730+9800+9250) = 89930</b><br><br><b>Type ‘start’ to go back to main menu</b>",
"o",
"<b>OEC<br>Fee : 1250 <br>Fee already paid to Entrance Commissioner :1000 <br> →Fee to be paid at Director’s Account : 250<br>Examination Fee:100<br>Miscellaneous Fee : 9800<br>Hostel Fee:9250<br>Total : (250+100+9800+2250) = 12400</b><br><br><b>Type ‘start’ to go back to main menu</b>",
"w",
"<b> Merit Seat <br><br>Fee already paid to Entrance Commissioner : 10000 <br> →Fee to be paid at Director’s Account :33150<br>Examination Fee:7730<br>Miscellaneous Fee : 9800<br>Hostel Fee:9250<br> →Total : (7730+9800+9250) = 26780<br></b><b><br><br><b>Type ‘start’ to go back to main menu</b>",

"h",
"<b>Hostel <b>Are you a Girl or Boy?<br>g Girl<br>b Boy</b>",
"g",
"<b>Name: Shahnas Hostel<br>Location: Inside the college</b><br><br><b>Type ‘start’ to go back to main menu</b>",
"b",
"<b>Name: Zulu's Hostel<br>Location: Povval</b><br><br><b>Type ‘start’ to go back to main menu</b>",
"d",
"<b>CSE-A : Dr. Sarith Divakar M - 📞 +91 9946760222<br> CSE-B : Prof. Jayalakshmi - 📞 +91 9645238136<br> IT : Prof. Nishy Reshmi S - 📞 +91 9961282630<br> CE : Dr. Anjali M S - 📞 +91 9496251434<br> ECE : Prof. Nishanth Augustine - 📞 +91 9744744639<br> EEE : Prof. Arun S Mathew - 📞 +91 9446588123<br>ME : Prof. Sajan Jerome - 📞 +91 9400540958</b><br><br><b>Type ‘/start’ to go back to main menu</b>",

"n",
"<b>1 Fee <br>2 College Bus Details <br>3 Department Contacts</b>",
"1",
"<b>4 Merit Seat <br>5 Management Seat<br>6 OEC <br><br>7 Fee Waiver</b>",
"4",
"<b> Merit Seat <br><br>Fee : 43150 <br>Fee already paid to Entrance Commissioner : 10000 <br> →Fee to be paid at Director’s Account :33150<br>Examination Fee:7730<br>Miscellaneous Fee : 9800<br>→Total :(33150+7730+9800) = 50680</b><br><br><b>Type ‘start’ to go back to main menu</b> ",
"5",
"<b> Management Seat <br>Fee : 73150 <br> Fee already paid to Entrance Commissioner : 10000 <br> →Fee to be paid at Director’s Account :63150<br>Examination Fee:7730<br>Miscellaneous Fee : 9800<br>→Total :(63150+7730+9800) = 80680</b><br><br><b>Type ‘start’ to go back to main menu</b>",
"6",
"<b>OEC<br>Fee : 1250 <br> Fee already paid to Entrance Commissioner :1000 <br> →Fee to be paid at Director’s Account : 250<br>Examination Fee:100<br>Miscellaneous Fee : 9800<br>→Total : (250+100+9800) = 10150<br><br><b>Type ‘start’ to go back to main menu</b>",
"7",
"<b> Fee Waiver <br><br>Fee already paid to Entrance Commissioner : 10000 <br> →Fee to be paid at Director’s Account :33150<br>Examination Fee:7730<br>Miscellaneous Fee : 9800<br>→Total :(7730+9800) = 17530</b><br><br><b>Type ‘start’ to go back to main menu</b> ",

"2",
"<b> Bus Details <br><br>8 From Nileshwaram Side<br>9 From Kasaragod Side</b>",
"8",
"<b>From Nileshwaram Side(Place | Time | Rate)<br>Nileshwaram | 8:05 |₹16,759<br>Padannakkad | 8:10 | ₹14,914<br>Kanhangad South | 8:15 |₹14,069<br>Kanhangad New Bus Stand | 8:17 | ₹13,530<br>Kanhangad Bus Stand| 8:20 | ₹13,069<br>Mavungal | 8:30 | ₹12,685<br>Pullur | 8:35 |₹11,685<br>Chalingal | 8:40 | ₹10,071<br>Periya | 8:45 |₹8,380<br>Periyattadukkam | 8:50 | ₹7,457<br>Mailatty | 8:53 |₹6,381<br>Poinachy | 8:56 | ₹5,843<br>Chattanchal | 9:00 |₹5,459<br>Bevinja | 9:05 | ₹4,151<br>Cherkala | 9:10 | ₹2,845<br>College |9:20</b><br><br><b>Type ‘start’ to go back to main menu</b>",
"9",
"<b>From Kasaragod Side(Place | time | Rate)<br>Pallikkara | 8:15 |₹9,917<br>Bekal | 8:20 | ₹9,302<br>Palakkunnu | 8:25 | ₹8,764<br>Udma |8:30 | ₹8,380<br>Kalanad | 8:35 | ₹7,841<br>Melparamba | 8:40 |₹7,457<br>Chaliyancode | 8:45 | ₹7,150<br>Chemnad | 8:50 |₹6,919<br>Kasaragod(Railway Station) | 8:40 |₹7,457<br>Kasaragod(mallikarjuna) | 8:40 | ₹7,150<br>Kasaragod New Bus Stand | 8:55 | ₹6,535<br>Vidyanagar | 9:00 | ₹4,690<br>Nalam Mile | 9:05 |₹3,767<br>Cherkala | 9:10 | ₹2,845<br>College | 9:20</b><br><br><b>Type‘start’ to go back to main menu</b>",
"3",
"<b>CSE-A : Dr. Sarith Divakar M - 📞 +91 9946760222<br> CSE-B : Prof. Jayalakshmi - 📞 +91 9645238136<br> IT : Prof. Nishy Reshmi S - 📞 +91 9961282630<br> CE : Dr. Anjali M S - 📞 +91 9496251434<br> ECE : Prof. Nishanth Augustine - 📞 +91 9744744639<br> EEE : Prof. Arun S Mathew - 📞 +91 9446588123<br>ME : Prof. Sajan Jerome - 📞 +91 9400540958</b><br><br><b>Type ‘start’ to go back to main menu</b>",

]


trainer.train(conversation)
