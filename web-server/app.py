from flask import Flask

app = Flask(__name__)

@app.route("/personal")
def personal():
    return "Ik ben een energiek persoon die graag bijleert en de puntjes op de i zet.De ideale job voor mij heeft mogelijkheden tot bijscholen, flexibele werkuren en een gezonde werkdruk!"

@app.route("/experience")
def experience():
    return "2016 – 2018 I-Fitness Hasselt Sales Consultant Allround Medewerker"

@app.route("/education")
def education():
    return "2018 – heden Professionele Bachelor Toegepaste Informatica\n2015 – 2016 Diploma Secundair onderwijs: Business Support"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')