# This is a sample Python script.


import numpy as np
import pandas as pd

from margin import tpm_margin_reader
from margin import tpm_margin_processor
from margin import tpm_margin_writer

df = tpm_margin_reader.get_margin_records_from_file()
df = tpm_margin_processor.process(df)
df = tpm_margin_writer.create_margin_file(df)
print(df.to_string())