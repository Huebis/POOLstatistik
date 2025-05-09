import pandas as pd
from pyaxis import pyaxis


def Input():

    # Path to your .px file
    px_file_path = "px-x-1702020000_105.px"

    # Parse the .px file
    px_data = pyaxis.parse(px_file_path, encoding='ISO-8859-2')

    # Access the data as a pandas DataFrame
    df = pd.DataFrame(px_data['DATA'])

    # Display the first few rows of the DataFrame
    print(df.head(800))
    return df





