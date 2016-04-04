# coding=utf-8
""" These class and method definitions allow for manipulation of city names.
    They will be useful in the solving of various puzzles for the NPR Sunday Puzzle.
    Need to update my input files
"""


class City:
    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    def __init__(self, name=None, city_type=None, state_name=None, country_name=None):
        self.name         = name
        self.city_type    = city_type
        self.state_name   = state_name
        self.country_name = country_name
        # print("City fields:", self.name, self.city_type, self.state_name, self.country_name)

    @property
    def num_vowels(self):
        count = 0
        for i in range(len(self.name)):
            if self.name.lower()[i] in City.VOWELS:
                count += 1
        return count

    @property
    def num_consonants(self):
        count = 0
        for i in range(len(self.name)):
            if self.name.lower()[i] in City.CONSONANTS:
                count += 1
        return count

    @property
    def num_letters(self):
        # Return the number of letters in the city name excluding spaces
        return len(self.name.replace(" ", ""))

    @property
    def alphabetized_letters(self):
        # Return the name with the letters alphabetized
        alpha_city = "".join(sorted(self.name.lower()))
        return alpha_city.replace(" ", "")


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
        print("{0} ({4}) has {1} letters, {2} vowels and {3} consonants".format(city_list[i].name, city_list[i].num_letters,
                                                             city_list[i].num_vowels, city_list[i].num_consonants,\
                                                             city_list[i].alphabetized_letters))


# Check for interactive session
if __name__ == '__main__':
    # execute main program
    main()
