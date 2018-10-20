from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    pBberry = request.form['blackberry']
    pSberry = request.form['strawberry']
    pRberry = request.form['raspberry']
    pApple = request.form['apple']
    pFirstname = request.form['first_name']
    pLastname = request.form['last_name']
    pStudentid = request.form['student_id']
    pSum = int(request.form['strawberry']) + int(request.form['blackberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    return render_template("checkout.html",blackberry=pBberry,strawberry=pSberry,raspberry=pRberry,apple=pApple,first_name=pFirstname,last_name=pLastname,student_id=pStudentid,sum=pSum)
    
@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)