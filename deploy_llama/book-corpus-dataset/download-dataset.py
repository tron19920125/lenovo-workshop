# import library to parse command line arguments
import argparse, os, json

parser = argparse.ArgumentParser()
# add an argument to specify a dataset name to download
parser.add_argument("--dataset", type=str, default="bookcorpus", help="dataset name")
# add an argument to specify the directory to download the dataset to
parser.add_argument(
    "--download_dir",
    type=str,
    default="./",
    help="directory to download the dataset to",
)
args = parser.parse_args()

# create the download directory if it does not exist
if not os.path.exists(args.download_dir):
    os.makedirs(args.download_dir)

# import hugging face datasets library
from datasets import load_dataset

# load the split of the dataset
split = "train"
print(f"Loading {split} split of {args.dataset} dataset...")
# load the split of the dataset
dataset = load_dataset(args.dataset, split=split, streaming=True, trust_remote_code=True)
dataset = dataset.shuffle()
dataset = dataset.take(5)
# save the split of the dataset to the download directory as json lines file
with open(os.path.join(args.download_dir, f"{split}.jsonl"), "w") as f:
    for line in dataset:
        f.write(json.dumps(line) + "\n")
