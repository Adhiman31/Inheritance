import logging
logging.basicConfig(filename ="inh1.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

class inueron :

    def job_info(self,job_dict):
        try:
            logging.info('this function provides job role and annual salary expectations offered at inueron')
            for k,v in job_dict.items():
                logging.info("The Job Role is %s and Salary is %s",k ,v)
        except Exception as e:
            logging.error(e)

    def fee_structure(self,course_name):
        logging.info("this function gives the fee description as per chosen course")
        try:
            if course_name == 'FSDS':
                logging.info('the fees for FSDS course is 15000 INR')
            elif course_name == 'Big Data':
                logging.info('the fees for Big Data course is 10000 INR')
            elif course_name == 'SQL':
                logging.info("the fees for SQL course is 5000 INR")
            else:
                logging.info("Sorry , currently we do not have the course you are looking for")
        except Exception as e:
            logging.info(e)


i = inueron()
logging.info("this is inueron class object:  %s",i)

class students(inueron) :


    def stud_info(self):
        try :
            logging.info("This is function under class student")
        except Exception as e:
            logging.error(e)

s = students()
logging.info("this is student class object : %s",s)
logging.info("calling inueuron class functions using students class objects....")
s.job_info({'Data Scientist' : 1200000 ,'SQL Developer':100000 ,'Data Engineer' : 130000 ,'Data Analyst' :900000})
s.fee_structure('FSDS')
s.fee_structure('Data Analytics')

s.stud_info()
















