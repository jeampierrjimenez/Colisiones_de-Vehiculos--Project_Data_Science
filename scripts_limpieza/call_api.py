import requests
import json
import pandas as pd
import numpy as np


def api_to_df_upper_columns(url):
  response = requests.get(url)
  df = pd.DataFrame(response.json())
  df.columns = df.columns.str.upper()
  return df

def api_to_df(url):
  response = requests.get(url)
  df = pd.DataFrame(response.json())
  return df
