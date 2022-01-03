from flask import Flask,render_template,request
from flask_cors import cross_origin
import support
import pickle
import numpy as np

main = Flask(__name__,template_folder="templates")
model = pickle.load(open("./model.pkl", "rb"))
@main.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("Cofe-AI.html")

@main.route("/result",methods=['GET', 'POST'])
@cross_origin()
def result():
	cough = request.form.get("cough")
	cough = int(support.bin_val(cough))
	fever = request.form.get("fever")
	fever = int(support.bin_val(fever))
	sore_throat = request.form.get("sore_throat")
	sore_throat = int(support.bin_val(sore_throat))
	shortness_of_breath = request.form.get("shortness_of_breath")
	shortness_of_breath = int(support.bin_val(shortness_of_breath))
	head_ache = request.form.get("head_ache")
	head_ache = int(support.bin_val(head_ache))
	gender = int(request.form.get("gender"))
	test_indication = int(request.form.get("test_indication"))
	age = request.form.get("age")

	if(int(age)>60):
		age=1
	else:
		age=0
	
	data=np.array([cough,fever,sore_throat,shortness_of_breath,head_ache,age,gender,test_indication]).reshape(1,-1)

	res=model.predict(data)
	
	if(int(res)==0):
		return render_template("nresult.html")
	return render_template("presult.html")




if __name__=='__main__':
	main.run(debug=True)