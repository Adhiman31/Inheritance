import logging
logging.basicConfig(filename ="inh3.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

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

    def affliate(self):
        try:
            logging.info("this is the function under class course")
        except Exception as e:
            logging.info(e)


c = course()
logging.info("this is course class object:  %s",c)

class jobs:

    def job_info(self,job_dict):
        try:
            logging.info('this function provides job role and annual salary expectations offered at inueron')
            for k,v in job_dict.items():
                logging.info("The Job Role is %s and Salary is %s",k ,v)
        except Exception as e:
            logging.error(e)

    def affliate(self):
        try:
            logging.info("this is the function under class jobs...")
        except Exception as e:
            logging.info(e)

j = jobs()
logging.info("this is jobs class object:  %s",j)

class multi(course,jobs):
    pass




t = multi()
logging.info("this is multi class object:  %s :",t)

logging.info("Now the function affliate is under both class Parent classes courses and jobs "
             "we will try to access this function with object of class_type and see which class function is fetched...")

logging.info(t.affliate())

logging.info("preference is given to the first class which is inherited , "
             "and in this case it is class course so function affliate fetched is of class course...")
