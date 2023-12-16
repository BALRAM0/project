import random, requests, webbrowser
print("Hi! Welcome to Seth Jai Parkash Polytechnic, Damla\nTo get started with SJPP Bot, enter 'Start' or 'Begin': ")

bot_name = "" 
college_info = "Seth Jai Parkash Polytechnic, Damla (Yamuna Nagar) is a constituent of prestigious Seth Jai Parkash Mukand Lal Institutions of Knowledge and Service and was established in the year 1980 to disseminate value based quality technical education. Sh.Ashok Kumar – the Chairman of the Society and Governing Body is a leading industrialist, philanthropist of Northern India managing 27 institutions of Knowledge & Service spread in Yamuna Nagar, Radaur, Ghaziabad. The institute is affiliated to Directorate of Technical Education, Haryana and approved by All India Council for Technical Education, New Delhi." 
course_info = "Courses available here are:\n1.	Computer Engineering\n2.	Chemical Engineering (Pulp and Paper)\n3.	Electronics and Communication Engg.\n4.	Electrical Engg."
extracurricular = "During the course of its long journey, the Polytechnic has achieved many a milestones in academics, sports and extra-curricular activities and its alumni have made a mark in different spheres related to public service and life.\nBest Polytechnic Awards\n\nAdjudged best polytechnic of Northern India by NITTTR, Chandigarh for the year 2002-03.\nAdjudged best polytechnic of Northern India by NITTTR, Chandigarh for the year 2008-09.\nHave been awarded the Sardar Ajmer Singh Sarao Memorial Running Trophy for Best Polytechnic of Haryana in the year 2010-11.\nThe Polytechnic has been Adjudged outstanding polytechnic of Northern India by NITTTR, Chandigarh for the year 2014-15."
location = ""

resp = {
    "getting started" : ["Hi there, let me introduce you to our college {0}".format(college_info), "Hii!\nNice to see you today\n Let me introduce you to our college\n {0}".format(college_info),"Hiii\nSo to begin with anything today, I would like to introduce you to our college\n{0}".format(college_info)],
    "what's your name?": [ "You can call me {0}".format(bot_name), "My name is {0}".format(bot_name)],
    #"what's today's weather?": [ "The weather is {0}".format(monsoon), "It's {0} today".format(monsoon)], 
    "courses offered" : ["Here's a list of the same\n{0}".format(course_info), "{0}\nThese are the courses available".format(course_info)],
    "extracurricular achievements" : ["{0}".format(extracurricular)],
    "location" : "Webpage opened",
    "website" : "Webpage opened",
    "": ["Hey! Are you there?", "If you want to end this conversation then enter 'quit' or 'stop'"],
    "default": ["This is a default message"]}

def res(message):
    if message in resp: 
        bot286_message = random.choice(resp[message])
    else: 
        bot286_message = random.choice(resp["default"])
    return bot286_message

def real(xtext): 
    if "start" in xtext or "begin" in xtext or "Hello" in xtext: 
        ytext = "getting started"
    elif "name" in xtext:
        ytext = "what's your name?"
    elif "course" in xtext: 
        ytext = "courses offered"
    elif "how to reach the institute" in xtext or "location" in xtext or "college on maps" in xtext:
        ytext = "location"
        webbrowser.open_new_tab("http://surl.li/eeiub")      
    elif "website" in xtext or "webpage" in xtext:
        ytext = "website"
        webbrowser.open_new_tab("https://www.sjpdamla.ac.in/")
    else:
        ytext = ""
    return ytext

def send_message(message): 
    #print((message)) 
    response = res(message) 
    print((response))

while True: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = real(my_input)
    if my_input == "exit" or my_input == 'end' or my_input == 'quit' or my_input == "stop": 
        break
    send_message(related_text)