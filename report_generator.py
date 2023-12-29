import pandas as pd
import openpyxl

class ReportGenerator:
    """
    Generates reports in CSV and Excel formats.
    """

    @staticmethod
    def generate_csv(data, filename):
        """
        Generates a CSV report.

        Args:
            data (list of lists): The data to write to the CSV file.
            filename (str): The name of the CSV file to create.
        """

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
