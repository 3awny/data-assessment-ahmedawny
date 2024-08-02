
from config import *
import pandas as pd
from services import DataAnalyzer

def get_data_analyzer():
    return DataAnalyzer('app/data/cleaned_data.csv')
