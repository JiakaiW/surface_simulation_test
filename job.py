import sys
import json
import pickle
import surface_erasure_decoding


# This function can be run over condor
def main():
    counter = sys.argv[1]
    # Load Sample_decode_job instance
    with open(f'{counter}.pkl', 'rb') as f:
        job = pickle.load(f)
    # Get result back from Sample_decode_job instance
    result = job.sample_and_print_result()
    # Print result
    # Just let the printed messaged be loaded into the .out files automatically.
    json_str = json.dumps(result)
    sys.stdout.buffer.write(json_str.encode())

def decode_locally(counter):
    pass


if __name__ == '__main__':
    main()


