from flask import Flask, render_template,request
import getCriteriaAndResult

app = Flask(__name__)
@app.route('/', methods=["POST","GET"])
def index():
    return render_template('index.html')
@app.route('/getCriteria',methods=["POST"])
def generateCriteria():
    table = ""
    print(request.form)
    if request.method == 'POST':
        table = getCriteriaAndResult.get_criteria(request.form["question"])
        print(table)
        # finalTable =getCriteriaAndResult.getResults(table)
        table2=getCriteriaAndResult.get_results(table)
    return render_template('/index.html', table=table2)

    # results_question = f"Language models that meet the following criteria: {criteria}"
    # results = get_results(results_question)
    # print(results)

if __name__ == "__main__":
    # app.run(app,port=8000)
    app.run(debug=True)