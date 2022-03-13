import argparse
import random

def generate_boys(female_ratio : float):

    # run loop for as long as random number is greater than
    # female_ratio, incrementing boy counter with each iteration
    boys = 0
    while ( random.random() > female_ratio):
        boys += 1

    return boys


def run_generation(num_families : int, female_ratio : float):
    total_boys = 0
    
    for n in range(num_families):
        total_boys += generate_boys(female_ratio)

    print(f"Girls: {num_families} \t Boys: {total_boys}")


def main():
    parser = argparse.ArgumentParser(
        """Code for simulating problem 6.7 (The Apocalypse) in Cracking the Coding Interview by McDowell""")
    parser.add_argument("--num_families", type=int, default=1000)
    parser.add_argument("--female_ratio", type=float, default=0.5)

    args = parser.parse_args()


    num_families = args.num_families
    female_ratio = args.female_ratio

    run_generation(num_families, female_ratio)

if __name__ == "__main__":
    main()
    


