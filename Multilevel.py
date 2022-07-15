import logging
logging.basicConfig(filename ="inh2.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

class course:

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

c = course()
logging.info("this is course class object:  %s",c)

class jobs(course):

    def job_info(self,job_dict):
        try:
            logging.info('this function provides job role and annual salary expectations offered at inueron')
            for k,v in job_dict.items():
                logging.info("The Job Role is %s and Salary is %s",k ,v)
        except Exception as e:
            logging.error(e)

j = jobs()
logging.info("this is jobs class object:  %s",j)

class internship(jobs):

    def disp_intern(self):
        try:
            logging.info("Display the list of internship offered at ineuron")
            for s in type_of_internship:
                logging.info(s)
        except Exception as e:
            logging.error(e)

i = internship()
logging.info("this is internship class object:  %s",i)

logging.info("Since class jobs inherited the properties of class course , we will try to access/call function inside course class...")
logging.info(j.fee_structure('FSDS'))

logging.info("Since class internship inherited class jobs , and jobs already inherited class course , "
             "we will try access functions of both with the object of class internship.....")
logging.info(i.job_info({'Data Scientist' : 1200000 ,'SQL Developer':100000 ,'Data Engineer' : 130000 ,'Data Analyst' :900000}))
logging.info(i.fee_structure('SQL'))




