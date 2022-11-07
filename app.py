from flask import Flask

app=Flask(__name__)



@app.route("/",methods=['GET','POST'])
def index():
    return "The CI CD pipelining has been established"

if __name__=="__main__":
    app.run(debug=True)
    
