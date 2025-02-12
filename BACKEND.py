def search_faq(question,faq_data):
    for key in faq_data:
        if question.lower()in key.lower():
            return faq_data[key]
    return "Sorry,I don't have an answer to that question."


def main():
    faq={
#1
"hi":
    "Hello",
#2
"how are you?":
    "I'm doing well,thank you.",
#3
"what is your name?":
    "My name is SRMBOT.",
#4
"what type of questions can you answer?":
      "I can answer questions related to the admission proceses and general admission related quaries.",
#5
"what are the admission requirements for SRM?":
    "Admission requirements vary by programbut generally include GPA,standardized test scores,letters of recommendation,and essays.",
#6
"what documents are needed for admission in SRM?":
    "The main documnets which are required for admission in SRMIST are 10th passing certificate,12th passing certificate,SRM entrance result and any valid government ID proof.",
#7
"what are different courses of study that are available in SRMIST?":
    "The courses of study available in SRMIST are B.Tech,Hons,Medical,etc...",
#8
 "what is the tution fee at SRM?":
     "The tution fee varies at SRM depending upon the branch and specialization you opt for.",
#9
"what is the tution fee for engineering in SRM with CSE?":
    "The tution fee for engineering in SRM ranges from 3,00,000 to 4,50,000 depending upon the specialization a student opts for.",
#10
"how can I get admission in SRM for engineering?":
    "Admissions are open for engineering in SRMIST from April 1,2024. To apply for admissions you need to fill up the admission form of SRMIST and then appear for an entrance test. If you qualify the entrance test and pass the eligibility criteria of admissions then you can get admitted to SRM.",
#11
"from where can I download the admission form for admissions?":
    "The admission form for admissions can be downloaded from the official website of SRMIST.",
#12
"which branch has the best placement in SRM?":
    "The CSE branch has the highest placement in SRM ith 100% placement record and also having the highest package.", 
#13
"what specializations in CSE are available in SRM?":
    "There are a wide range of specializations that are available in CSE in SRM institute: Software,AL&ML,Cyber Security,Machine Learning,Data Analytics,CSBS,Gaming Technology,Cloud computing,etc..",
#14
"are accomodation facilities available in SRM?":
    "Yes,there are a wide range of accomodation facilities available inside SRM campus. One can choose type of hostels he/she wants to take admission in.",
#15
"how to book hostel in SRM?":
    "You can book hostel in SRM only after you have taken admission in SRM and have got your registeration number and admission confirmation letter.",
    
   #Add more FAQ pairs here                                               
    }
print("Welcome to the FAQ Chatbot!Ask me anything.")
print("Type 'exit' to quit.")
while True:
    user_input=input("You: ")
        
    if user_input.lower()=='exit':
        print("Exiting the FAQ Chatbot. Goodbye!")
        break
    reponse =search_faq(user_input,faq)
    print("SRMBOT:",reponse)
if __name__=="_main_":
    main()