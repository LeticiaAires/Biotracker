import pandas as pd

def process_data(data, clean=True, aggregation=None):
    """
    Processes raw data into a DataFrame, performs cleaning, and provides statistics.

    Parameters:
        data (list of dicts or dict): Raw data to be processed into a DataFrame.
        clean (bool): Whether to perform data cleaning (default: True).
        aggregation (dict): A dictionary for aggregating data (default: None).
                            Format: {'column_name': 'aggregation_function'}.
                            Example: {'temperature': 'mean'}

    Returns:
        dict: A dictionary with the following keys:
            - 'summary': A statistical summary of the data.
            - 'dataframe': The processed DataFrame.
    """
    # Convert raw data to a DataFrame
    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        raise ValueError(f"Invalid data format: {e}")
    
    # Data cleaning: handle missing values
    if clean:
        df = df.fillna(method='ffill').fillna(method='bfill')  # Forward/backward fill missing values
    
    # Perform aggregation if specified
    if aggregation:
        try:
            aggregated_df = df.groupby(aggregation.keys()).agg(aggregation)
        except Exception as e:
            raise ValueError(f"Error during aggregation: {e}")
    else:
        aggregated_df = df

    # Return summary and processed data
    return {
        "summary": aggregated_df.describe(include="all").to_dict(),
        "dataframe": aggregated_df
    }
