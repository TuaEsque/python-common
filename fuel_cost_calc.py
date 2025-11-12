import argparse

# Controls CLI arguments for this script
parser = argparse.ArgumentParser()
parser.add_argument("-fc", "--fuel_cost", help="fuel cost in pence", type=float, required=True, metavar="")
parser.add_argument("-ml", "--mileage", help="mileage covered", type=float, required=True, metavar="")
parser.add_argument("-mpg", "--miles_per_gallon", help="average mpg", type=float, required=True, metavar="")
args = parser.parse_args()
print(f"£{round(((args.mileage / args.miles_per_gallon) * 4.54609) * args.fuel_cost) / 100}")
quit()