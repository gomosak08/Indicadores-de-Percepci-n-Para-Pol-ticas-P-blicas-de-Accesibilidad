from fastai.learner import load_learner
import pandas as pd

def predict_and_save(learner_path: str, input_file: str, output_file: str, columns_to_use: list):
    """
    Load a FastAI learner, make predictions on a dataset, and save the results to an Excel file.
    
    Parameters:
    - learner_path (str): Path to the trained FastAI model (`.pkl` file).
    - input_file (str): Path to the input Excel file containing the data.
    - output_file (str): Path where the output Excel file with predictions will be saved.
    - columns_to_use (list): List of column names to be used as input features.
    
    Returns:
    - None: The predictions are saved directly to the specified `output_file`.
    """
    # Load the trained learner
    learner = load_learner(learner_path)

    # Load the input Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Select the columns to be used for prediction
    df = df[columns_to_use]

    # Prepare a DataLoader for the DataFrame
    test_dl = learner.dls.test_dl(df)

    # Get predictions for all rows
    predictions = learner.get_preds(dl=test_dl)

    # Extract predicted values
    predicted_values = predictions[0].numpy()

    # Flatten predicted values if needed (e.g., regression outputs)
    predicted_classes = predicted_values.flatten()

    # Add predictions to the DataFrame
    df['Predicted'] = predicted_classes

    # Save the DataFrame with predictions to an Excel file
    df.to_excel(output_file, index=False)

    print(f"Predictions saved to {output_file}")
