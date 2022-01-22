import os
from pathlib import Path
import uuid
import random
import subprocess
import time
from faker import Faker
fake = Faker()


def load_langs(path):
    results = []
    master_records = []
    for root, dirs, files in os.walk(path):
        for file_ in files:
             split_tup = os.path.splitext(file_)
             file_extension = split_tup[1]
             results.append(os.path.join(root, file_))
        for r in results:
            p = Path(r)
            parts = list(p.parts)
            master_records.append({r : file_extension})
    return master_records

def make_dyn_folder():
    dynamic_folder_name = str(uuid.uuid4())
    os.mkdir(dynamic_folder_name)
    return dynamic_folder_name


def write_file(file_list):
    dirc = make_dyn_folder()
    for f in file_list:
        for k,v in f.items():
            with open(f"{k}", "r") as infile:
                try:
                    content = infile.readline()
                    with open(f"{dirc}/{str(uuid.uuid4())}{v}", "w") as outfile:
                        outfile.writelines(content)
                except:
                    pass


def git_push():
    while True:
        fuzzy = random.randint(1,5)
        time.sleep(fuzzy)
        add_command = "git add .".split()
        subprocess.run(add_command, shell=True, check=True)
        subprocess.run(['git', 'commit', '-a','--allow-empty-message', '-m', ''], shell=True, check=True)
        subprocess.run(["git", "push", "origin"], shell=True, check=True)


def actor_init():
    random_file_sample = random.sample(load_langs("lang_refs"), random.randint(1, 20))
    write_file(random_file_sample)
    git_push()

actor_init()