from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exceptiom")

    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)    
        logging.info("We are testing logging module")
    return "[Updated] The CI CD pipelining has been established"


if __name__=="__main__":
    app.run(debug=True)
    
