from datetime import datetime
chat = True
hellointent=["hello","hi","hey","wassup"]
while chat == True:
    user = input ("Enter message:").lower()
    if user in hellointent: 
        print("hello")
    elif user == "bye":
        print("have a great day")
        chat = False
    elif user.startswith("="):
        print(eval(user[1:]))
    elif "date" in user:
        dt = datetime.now()
        print(dt.strftime("%d-%m-%Y,%a"))
    elif "time" in user:
        dt = datetime.now()
        print(dt.strftime("%H:%M:%S,%p"))
    else:
        print("how can i help you")