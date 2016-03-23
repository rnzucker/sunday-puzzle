# coding=utf-8
""" These class and method definitions allow for manipulation of city names.
    They will be useful in the solving of various puzzles for the NPR Sunday Puzzle.
"""


class City:
    VOWELS = "aeiou"
    CONSONANTS = "bcdghjklmnpqrstvwxyz"

    def __init__(self, name=None, city_type=None, state_name=None, country_name=None):
        self.name = name
        self.city_type = city_type
        self.state_name = state_name
        self.country_name = country_name
        # print("City fields:", self.name, self.city_type, self.state_name, self.country_name)

    def num_vowels(self):
        count = 0

        for i in range(len(self.name)):
            if self.name.lower()[i] in City.VOWELS:
                count += 1
        return count

    def num_consonants(self):
        count = 0

        for i in range(len(self.name)):
            if self.name.lower()[i] in City.CONSONANTS:
                count += 1
        return count

    def city_name(self):
        return self.name


def main():
    print("Working on classes")
    city_list = []
    city_file = open("cities.txt", "r")
    for each_city in city_file:
        one_city = each_city.rstrip().split("\t")
        if one_city[1] == "state":
            city_list.append(City(city_type="state", name=one_city[0], state_name=one_city[2]))
        elif one_city[1] == "world":
            city_list.append(City(city_type="world", name=one_city[0], country_name=one_city[2]))
        elif one_city[1] == "-":
            city_list.append(City(city_type="-", name=one_city[0], state_name=one_city[2]))
        else:
            print("Input error: bad city type field")
    print(len(city_list), "cities")

    for i in range(len(city_list)):
        print("City {0} has {1} vowels and {2} consonants".format(city_list[i].city_name(), city_list[i].num_vowels(), \
                                                                  city_list[i].num_consonants()))


# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
