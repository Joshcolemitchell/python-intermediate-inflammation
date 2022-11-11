#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os
from inflammation import models, views, serializers
from matplotlib import pyplot as plt

def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]
    
    
    for filename in InFiles:
        inflammation_data = models.load_csv(filename)
        print(args.outfile)
        print(args.view)
        if args.view == 'visualize':
            view_data = {
                'average': models.daily_mean(inflammation_data),
                'max': models.daily_max(inflammation_data),
                'min': models.daily_min(inflammation_data),
            }

            views.visualize(view_data)
            plt.show()

        elif args.view == 'record':
            patient_data = inflammation_data[args.patient]
            observations = [models.Observation(day, value) for day, value in enumerate(patient_data)]
            patient = models.Patient('UNKNOWN', observations)

            views.display_patient_record(patient)
            
        elif args.view == 'loadJSON':
            # Check that the JSON file is there. if not tell the user. 
            # load data from the JSON file
            assert os.path.exists(args.outfile),"Patient " + str(args.outfile) + " JSON file does not exist, please make one"
            patients_new = serializers.PatientJSONSerializer.load(args.outfile)
            # Check that we've got the same data back
            print(patients_new[0])
            #for patient_new, patient in zip(patients_new, patients):
            #   views.display_patient_record(patients) 

              
      
        elif args.view == 'saveJSON':    
            # save data to a JSON file
            print("saved to " + args.outfile)
            patient_data = inflammation_data[args.patient]
            observations = [models.Observation(day, value) for day, value in enumerate(patient_data)]
            patient = [models.Patient(args.outfile[:-5], observations)]
            serializers.PatientJSONSerializer.save(patient, args.outfile)
        
        #view_data = {'average': models.daily_mean(inflammation_data), 'max': models.daily_max(inflammation_data), 'min': models.daily_min(inflammation_data)}

        #views.visualize(view_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')
    
    parser.add_argument(
        '--outfile',
        type=str,
        default='UNKNOWN.json',
        help='where we want to save or load our JSON files')
        
    parser.add_argument(
        '--view',
        default='visualize',
        choices=['visualize', 'record','loadJSON','saveJSON'],
        help='Which view should be used?, if you want to save to JSON profide filename and path /home/filename')

    parser.add_argument(
        '--patient',
        type=int,
        default=0,
        help='Which patient should be displayed?')
    
    args = parser.parse_args()

    main(args)
