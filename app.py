import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
habits=["Test habit", "habit 2"]

#Enables the date_range function to be called from every template
@app.context_processor
def add_date_range():
    #Sets the dates so we have 3 days before the current day and 3 days following the current day, the current day being in the middle
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates
    
    return {"date_range": date_range}

@app.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()
    return render_template("index.html", habits=habits, title="Habit Tracker - Home", selected_date=selected_date)

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template("add_habit.html", title="Habit Tracker - Add Habit", selected_date=datetime.date.today())