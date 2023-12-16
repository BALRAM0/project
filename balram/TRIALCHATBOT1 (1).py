import random, requests, webbrowser
print("Hi! Welcome to Seth Jai Parkash Polytechnic, Damla\nTo get started with SJPP Bot, enter 'Start' or 'Begin'\nTo get a list of operations you can perform, enter 'operations': ")

bot_name = "SJPP ka Bhoot" 
college_info = "Seth Jai Parkash Polytechnic, Damla (Yamuna Nagar) is a constituent of prestigious Seth Jai Parkash Mukand Lal Institutions of Knowledge and Service and was established in the year 1980 to disseminate value based quality technical education. Sh.Ashok Kumar – the Chairman of the Society and Governing Body is a leading industrialist, philanthropist of Northern India managing 27 institutions of Knowledge & Service spread in Yamuna Nagar, Radaur, Ghaziabad. The institute is affiliated to Directorate of Technical Education, Haryana and approved by All India Council for Technical Education, New Delhi." 
course_info = "Courses available here are:\n1.	Computer Engineering\n2.	Chemical Engineering (Pulp and Paper)\n3.	Electronics and Communication Engg.\n4.	Electrical Engg."
extracurricular = "During the course of its long journey, the Polytechnic has achieved many a milestones in academics, sports and extra-curricular activities and its alumni have made a mark in different spheres related to public service and life.\nBest Polytechnic Awards\n\nAdjudged best polytechnic of Northern India by NITTTR, Chandigarh for the year 2002-03.\nAdjudged best polytechnic of Northern India by NITTTR, Chandigarh for the year 2008-09.\nHave been awarded the Sardar Ajmer Singh Sarao Memorial Running Trophy for Best Polytechnic of Haryana in the year 2010-11.\nThe Polytechnic has been Adjudged outstanding polytechnic of Northern India by NITTTR, Chandigarh for the year 2014-15."
operations = "1. Get Started\n2. About Bot\n3. Courses offered\n4. Extracurricular Achievements\n5. Location\n6. Website\n7. Contact Us\n8. About departments"
computerdeptt = "The diploma course in computer engineering focuses on transforming its students into professionals in the area of computer engineering. The main aim is to impart knowledge to the students in the field of computer hardware as well as in software. Apart from the core subjects, the students can also choose from a pool of elective subjects – Java,.NET- that deepen their expertise in the development of application software. In addition the students in the course are made proficient with applications of emerging technologies such as Web Designing, Computer Network and Network Securities comprising areas like cyber securities, ethical hacking, PHP."
chemicaldeptt = "Chemical engineers profile is in the sphere of research, design, and development of chemical processes and equipment to oversee the operation and maintenance of industrial chemical, plastics, pharmaceutical, resource, pulp and paper, Petroleum Refinery, food processing plants and perform duties related to chemical quality, control, environmental protection and biochemical engineering. Chemical engineers are employed in a wide range of manufacturing and processing industries, consulting firms and government sector"
ecedeptt = "The diploma course in electronics and communication engineering imparts strong theoretical foundations and practical learning to its students on electronic devices as well as rigorous training in design and development of such devices and their applications. The course offers a wide spectrum of elective subjects that covers the application of sophisticated technologies. In addition to common core subjects offered in the course, the students can choose from other elective subjects with an aim to sharpen their technical expertise."
contact_info = "For any type of information please contact: \nE-Mail : principal@sjpdamla.ac.in\nPhone : (O) 01732-282444\n+91-94160-25444\n +91-82959-05291"
scholarships_offered = "Scholarship is available to students to support full-time study at Seth Jai Parkash Polytechnic. Each year several scholarships are provided to the students through Government schemes and several societies or agencies. Besides these several scholarships in the form of fee remission to the needy and Cash awards to the outstanding students and interest free study loans are given by the management of Seth Jai Parkash Polytechnic.\nBackward Caste Scholarship\nScheduled Caste Scholarship from GPW Ambala\nScheduled Caste Scholarship from District Welfare Officer, Yamuna Nagar\nIPPTA Scholarship\nHSCS Scholarship\nSCSP Scholarship from Government of India\nMinority Post-Matric Scholarship\nWakf Board Scholarship\nMerit Based Cash Award to Girls Toppers\nHandicapped Scholarship\nMerit-Cum-Means Scholarships to Class Toppers in every semester\nPost-Matric Scholarship to other state students\nAmbedkar Medhavi Chhatravriti Yojna by the Government\nCash Award to Diploma Holders with more than 80% marks given by Management\nCash Award to Topper of the Institute by the Management (Given separately for First Year, Second Year, Third Year)\nInterest Free study loan to the poor and needy students of the Polytechnic\nScholarship by Guru Harkrishan Educational Society\nMahindra & Mahindra Merit Scholarship"
resp = {
    "getting started" : ["Hi there, let me introduce you to our college {0}".format(college_info), "Hii!\nNice to see you today\n Let me introduce you to our college\n {0}".format(college_info),"Hiii\nSo to begin with, I would like to introduce you to our college.\n{0}".format(college_info)],
    "what's your name?": [ "You can call me {0}".format(bot_name), "My name is {0}".format(bot_name)], 
    "courses offered" : ["Here's a list of the same\n{0}".format(course_info), "{0}\nThese are the courses available".format(course_info)],
    "extracurricular achievements" : ["{0}".format(extracurricular)],
    "contact us" : ["{0}".format(contact_info)],
    "location" : ["Webpage opened"],
    "website" : ["Webpage opened"],
    "computer engineering" : ["{0}".format(computerdeptt)],
    "chemical engineering" : ["{0}".format(chemicaldeptt)],
  #  "principal" : ["{0}".format()],
    "scholarships" : ["{0}".format(scholarships_offered)],
    "operations" : ["{0}".format(operations)],
    "electronics and communication engineering" : ["{0}".format(ecedeptt)],
    "": ["Enter a valid question","Sorry, I didn't understand", "If you want to end this conversation then enter 'quit' or 'stop'"],
    "default": ["This is a default message"]}

def res(message):
    if message in resp: 
        bot286_message = random.choice(resp[message])
    else: 
        bot286_message = random.choice(resp["default"])
    return bot286_message

def real(xtext): 
    if "start" in xtext or "begin" in xtext or "hello" in xtext or "hi" in xtext or "hey" in xtext or "hlo" in xtext or "yo" in xtext: 
        ytext = "getting started"
    elif "name" in xtext or "about bot" in xtext or "bot" in xtext:
        ytext = "what's your name?"
    elif "course" in xtext: 
        ytext = "courses offered"
    elif "how to reach" in xtext or "location" in xtext or "college on maps" in xtext or "maps" in xtext:
        ytext = "location"
        webbrowser.open_new_tab("http://surl.li/eeiub")
    elif "website" in xtext or "webpage" in xtext:
        ytext = "website"
        webbrowser.open_new_tab("https://www.sjpdamla.ac.in/")
    elif "principal" in xtext or "director" in xtext:
        ytext = "principal"
    elif "scholarship" in xtext:
        ytext = "scholarships"
    elif "extracurricular" in xtext or "achievements" in xtext or "awards" in xtext or "prizes" in xtext:
        ytext = "extracurricular achievements"
    elif "coe" in xtext or "computer" in xtext:
        ytext = "computer engineering"
    elif "ece" in xtext or "elctronics" in xtext:
        ytext = "electronics and communication engineering"
    elif "chem" in xtext or "chemical" in xtext:
        ytext = "chemical engineering"
    elif "operations" in xtext or "tasks" in xtext:
        ytext = "operations"
    else:
        ytext = ""
    return ytext

def send_message(message): 
    #print((message)) 
    response = res(message) 
    print((response))

while True: 
    my_input = input("Talk to Bot: ") 
    my_input = my_input.lower() 
    related_text = real(my_input)
    if my_input == "exit" or my_input == 'end' or my_input == 'quit' or my_input == "stop": 
        break
    send_message(related_text)