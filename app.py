from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.get_json(force=True)
    df = pd.DataFrame(data["data"])

    # Dummy forecast logic
    if "Revenue" in df.columns:
        df["Forecast"] = df["Revenue"] * 1.1
    else:
        df["Forecast"] = np.nan

    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
