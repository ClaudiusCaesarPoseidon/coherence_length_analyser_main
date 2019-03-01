import os
from coherence_length_analyser.lib import functions

max_back = -2500
max_for = 2500

path = functions.resource_path(os.path.join("data","motor_extrema.txt"))

try:
    with open(path, "r") as file:
        tmp = file.read().split("\n")
        max_back = int(tmp[0].split("=")[-1])
        max_for = int(tmp[1].split("=")[-1])
except FileNotFoundError:
    with open(path, "w") as file:
        file.write("max_back = -2500\nmax_for = 2500")
        max_back = -2500
        max_for = 2500
