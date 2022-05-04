from flask import Blueprint, request, jsonify, render_template, redirect, flash 

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipe")
def index():
    print("Recipe...")
    #return "Welcome Home"
    return render_template("recipe.html")


@recipe_routes.route("/recipe/form")
def recipe_form():
    print("RECIPE FORM...")
    return render_template("recipe_form.html")

# still editing
@recipe_routes.route("/recipe/generator", methods=["GET", "POST"])
def recipe_generator():
    print("Recipe Generator...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST":  # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)


    # country_code = request_data.get("country_code") or "US"
    # zip_code = request_data.get("zip_code") or "20057"

    # results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    # if results:
    #     flash("Weather Forecast Generated Successfully!", "success")
    #     return render_template("weather_forecast.html", country_code=country_code, zip_code=zip_code, results=results)
    # else:
    #     flash("Geography Error. Please try again!", "danger")
    #     return redirect("/weather/form")