import unittest
import pandas as pd
import random
from typing import List

from analytic_types.data_bucket import DataBucket
from tests.test_dataset import create_list_of_timestamps

class TestBucket(unittest.TestCase):

    def test_receive_data(self):
        bucket = DataBucket()
        data_val = list(range(6))
        timestamp_list = create_list_of_timestamps(len(data_val))
        for val in data_val:
            bucket.append_data(get_pd_dataframe([val], [1523889000000 + val]))
        for idx, row in bucket.data.iterrows():
            self.assertEqual(data_val[idx], row['value'])
            self.assertEqual(timestamp_list[idx], row['timestamp'])

    def test_max_size(self):
        bucket = DataBucket()
        data_val = list(range(10))
        timestamp_list = create_list_of_timestamps(len(data_val))
        bucket.set_max_size(5)
        bucket.append_data(get_pd_dataframe(data_val, timestamp_list))
        expected_data = data_val[5:]
        expected_timestamp = timestamp_list[5:]
        self.assertEqual(expected_data, bucket.data['value'].tolist())
        self.assertEqual(expected_timestamp, bucket.data['timestamp'].tolist())

if __name__ == '__main__':
    unittest.main()

def get_pd_dataframe(value: List[int], timestamp: List[int]) -> pd.DataFrame:
    if len(value) != len(timestamp):
        raise ValueError(f'len(value) should be equal to len(timestamp)')
    return pd.DataFrame({ 'value': value, 'timestamp': timestamp })
