from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result=""
    confidence=""
    treatment=""

    if request.method=="POST":

        fever=int(request.form["fever"])
        cough=int(request.form["cough"])
        fatigue=int(request.form["fatigue"])

        score=fever+cough+fatigue

        if score==3:
            result="High probability of Flu"
            confidence="85%"
            treatment="Rest, hydration and medication"

        elif score==2:
            result="Possible viral infection"
            confidence="65%"
            treatment="Take rest and drink warm fluids"

        elif score==1:
            result="Mild symptoms"
            confidence="40%"
            treatment="Monitor symptoms"

        else:
            result="Low probability of illness"
            confidence="20%"
            treatment="No major treatment needed"

    return render_template("index.html",result=result,confidence=confidence,treatment=treatment)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/ai")
def ai():
    return render_template("ai.html")


@app.route("/network")
def network():
    return render_template("network.html")


if __name__ == "__main__":
    app.run(debug=True)