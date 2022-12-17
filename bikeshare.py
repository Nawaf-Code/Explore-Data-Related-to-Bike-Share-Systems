"""
Description of project
Use Python to explore data related to bike share systems for three major cities in the
    -United States—Chicago
    -New York City
    -Washington
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("what data you would like to see: \n - Chicago \n - New York City \n - Washington \n your choice: ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid name, Please try again.\n\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print("Please Choose Month to Filter Data:")
        print(" -january     -february \n -march       -april \n -may         -june \n -all")
        month = input("your choice: ").lower()
        months_list = ['january','february','march','april','may','june','all']
        if month in months_list:
            break
        else:
            print("Invalid name, Please try again.\n\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("Please Choose Day to Filter Data:")
        print(" -monday      -tuesday \n -wednesday   -thursday \n -friday      -saturday \n -sunday      -all ")
        day = input("your choice: ").lower()
        days_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        if day in days_list:
            break
        else:
            print("Invalid name, Please try again.\n\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):#popular times of travel
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month is:", most_common_month)
    print("\n")

    # TO DO: display the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print("Most common Weekday is:", most_common_weekday)
    print("\n")

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common hour is:", most_common_hour)
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):#popular stations and trip
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: ", most_common_start_station)
    print("\n")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is:", most_common_end_station)
    print("\n")

    # TO DO: display most frequent combination of start station and end station trip
    filter_station = df.groupby(['Start Station','End Station']).size().sort_values(ascending = False).head(1)
    print("Most frequent combination of start station and end station is:\n ", filter_station)
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print("Total travel time is: ", travel_time_total)
    print("\n")

    # TO DO: display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print("Mean travel time: ", travel_time_mean)
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):#user info
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("counts of each user type:\n ", counts_of_user_types)
    print("\n")

    # TO DO: Display counts of gender
    if city != 'washington':
        counts_of_gender = df['Gender'].value_counts()
        print("counts of each gender:\n ", counts_of_gender)
        print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("Earliest year of birth:\n", earliest_year_of_birth)
        print("\n")

        most_recent_year_of_birth = int(df['Birth Year'].max())
        print("Most recent year of birth:\n",most_recent_year_of_birth)
        print("\n")

        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("Most common year of birth:\n",most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    index = 5
    check = True
    while True and check == True:
        print("Do you want  to see first 5 lines of raw data? \n - yes   - no")
        five_raw_data = input("your choice: ").lower()

        if five_raw_data == 'no':
            break
        elif five_raw_data == 'yes':
            print(df.iloc[:5])
            while True:
                print("Do you want to see more 5 lines of raw data? \n - yes   - no")
                complete_view = input("your choice: ").lower()
                if complete_view == 'yes':
                    print(df.iloc[index:index+5])
                    index += 5
                elif complete_view == 'no':
                    check = False
                    break
                else:
                    print("Invalid input, Please try again.\n\n")
        else:
            print("Invalid input, Please try again.\n\n")

def print_my_info():
    while True:
        ans = input("Would you like to see the information of programmer?").lower()
        if ans == 'yes':
            print("Name: Nawaf Saeed Alzuwaymil")
            print("Major: Computer Scince")
            print("Itersted: Data Scince and Machine Learning")
            print("Email: nawaf.zumlx@gmail.com")
            print("Github: Nawaf-Code")
        elif ans == 'no':
            break
        else:
            print("Invalid input, Please try again.\n\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        print_my_info()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
