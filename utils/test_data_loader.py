import yaml

def load_test_data(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

