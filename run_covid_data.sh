#! /bin/bash

echo "Activating airflow conda environment"
source ~/miniconda3/bin/activate airflow_env

echo "Changing directory to ~/Projects/India_Covid_Data/"
cd ~/Projects/India_Covid_Data/
echo "Current working directory - `pwd`"

echo "Executing python script to extract covid related data of Indian states"
python ~/Projects/India_Covid_Data/Covid_Data.py
