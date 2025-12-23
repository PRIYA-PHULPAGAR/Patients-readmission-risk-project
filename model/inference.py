import joblib
import os
import numpy as np

def model_fn(model_dir):
    """Load the trained model from the model_dir."""
    model_path = os.path.join(model_dir, "model.joblib")
    model = joblib.load(model_path)
    return model

def input_fn(request_body, request_content_type):
    """Parse the input JSON request."""
    import json
    data = json.loads(request_body)
    return np.array(data)

def predict_fn(input_data, model):
    """Make predictions."""
    prediction = model.predict(input_data)
    return prediction.tolist()

def output_fn(prediction, content_type):
    """Return the prediction as JSON."""
    import json
    return json.dumps(prediction)
