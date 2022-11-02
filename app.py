import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Hello')

from st_progress_text import st_progress


progress_text = '**_please_** be patient, at {value}%'
my_bar = st_progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.03)
    my_bar = st_progress(percent_complete + 1, text=progress_text)

my_bar.empty()

time.sleep(2)

from tqdm.auto import tqdm

for percent_complete in range(100):
    time.sleep(0.03)
    my_bar = st_progress(percent_complete + 1, text=tqdm.format_meter(percent_complete, 100, percent_complete*0.03))

st.success('Done!')
