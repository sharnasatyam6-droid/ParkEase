from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# USER LOGIN
# =========================

@app.route("/user-login")
def user_login():
    return "<h1>User Login</h1><p>User login page will be added soon.</p>"


# =========================
# ADMIN LOGIN
# =========================

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Temporary admin credentials
        if email == "admin@parkease.com" and password == "admin123":
            return redirect(url_for("admin_dashboard"))

        return render_template(
            "admin_login.html",
            error="Invalid email or password."
        )

    return render_template("admin_login.html")


# =========================
# ADMIN DASHBOARD
# =========================

@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)