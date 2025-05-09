import pandas as pd
from pyaxis import pyaxis


def Input(path):

    # Path to your .px file
    px_file_path = "path/to/your_file.px"

    # Parse the .px file
    px_data = pyaxis.parse(filepath=px_file_path, encoding='ISO-8859-2')

    # Access the data as a pandas DataFrame
    df = pd.DataFrame(px_data['DATA'])

    # Display the first few rows of the DataFrame
    print(df.head())

    # Optionally, save to CSV
    df.to_csv("output.csv", index=False)
