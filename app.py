from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Debugging: Print form values
        print("Form Values: ", request.form.values())
        
        features = [float(x) for x in request.form.values()]
        print("Features: ", features)  # Debugging: Print features list
        
        final_features = [features]
        print("Final Features: ", final_features)  # Debugging: Print final features
        
        prediction = model.predict(final_features)
        print("Prediction: ", prediction)  # Debugging: Print prediction result
        
        return render_template('index.html', prediction_text=f'Prediction: {prediction[0]}')
    except Exception as e:
        print("Error: ", e)  # Debugging: Print any errors that occur
        return render_template('index.html', prediction_text=f'An error occurred: {e}')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
