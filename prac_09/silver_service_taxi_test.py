from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2, 4)
    taxi.drive(18)
    fare = taxi.get_fare()
    assert fare == 148.50, f"Expected fare of 148.50 but got {fare}"
    print(taxi)


main()

