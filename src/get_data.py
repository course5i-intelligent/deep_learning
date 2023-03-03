import argparse
import os
import shutil
import logging
import yaml
import boto3
import pandas as pd 
import numpy as np 

def get_data(config_path):
    config=read_params(config_path)
    return config

def read_params(config_path):
    with open(config_path) as config:
        config=yaml.safe_load(config)
        return config

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config", default='params.yaml')
    passed_args=args.parse_args()
    try: 
        logging.info("\n *****")
        logging.info(f">>>Stage {STAGE} started <<")
        get_data(config_path=passed_args.config)
        logging.info(f">>>Stage {STAGE} completed <<")
    except Exception as e:
        logging.exception(e)
        raise e