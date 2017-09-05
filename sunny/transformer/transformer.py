import pandas
"""
This is the base class for the transformer used to convert the data format to a pandas dataframe
"""
class Transformer(object):

    @staticmethod
    def csv_to_pandas(*args , **kwargs):
        """
        Convert the csv to pandas to dataframe
        """
        return pandas.from_csv(*args , **kwargs)

    @staticmethod
    def pandas_to_csv(df , *args , **kwargs):
        """
        This is used to convert the pandas dataframe to the csv
        """
        return df.to_csv(*args , **kwargs)
    @staticmethod
    def pandas_to_json(df , *args , **kwargs):
        """
        This is used to convert the pandas dataframe to the json
        """
        return df.to_json(*args , **kwargs)


