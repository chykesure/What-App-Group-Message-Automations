import pywhatkit
import datetime

x = datetime.datetime.now()
zup = (x.strftime("%A"))

if zup != "Sunday" and zup != "Wednesday" and zup != "Tuesday":
    print('Not yet time Today nah ', zup)
else:
    pywhatkit.sendwhatmsg_to_group('E6tVdWWR1WyKX85R9tTLeI', 'Good day Sir, this is to remind you that our meeting will start by 8:30pm '
                                            'Every Wednesday and Sunday Evening. Thanks 💫✨', 14, 12)
