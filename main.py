from rich import print
import icalendar
import datetime
import os

def print_event_details(st: icalendar.Component, et: icalendar.Component, summary: icalendar.Component, start_cutoff: datetime = datetime.datetime.now().date(), end_cutoff: datetime = datetime.date(datetime.datetime.now().year, 12, 31)):
    """Prints the details of the event.

    Args:
        st (ical.Component): The ical component containing the start time of the event
        et (ical.Component): The ical component containing the end time of the event
        summary (ical.Component): The [summary] ical component containing the name of the event
        start_cutoff (datetime): This is the start time for the time frame in which you are looking for availability
        end_cutoff (datetime): this is the end time for the time frame in which you are looking for availability
    """
    start_str = str(st.dt)
    end_str = str(et.dt)
    start_dt = date_time_cons(start_str.split()[0])
    end_dt = date_time_cons(end_str.split()[0])

    if start_dt > start_cutoff and end_dt < end_cutoff:
        print(f"{summary}\n")

        print(f'This event starts at {start_dt} and ends at {end_dt}\n')

        print(f'{type(start_dt)}\n')

        print(f'Starts on a {start_dt.strftime("%A")} and ends on a {end_dt.strftime("%A")}\n')

def date_time_cons(dt_str : str) -> datetime.date:
    """ Create the datetime object by breaking up a string icalendar Component

    Args:
        dt_str (String): The string passed in that we break up
    Returns:
        A datetime object based on the broken up string
        will look like year-month-day
    """
    times = dt_str.split('-')
    year = int(times[0])
    month = int(times[1])
    day = int(times[2])
    date = datetime.date(year, month, day)
    return date


def print_cal_info(paths: str):
    """ Prints the info of the calendars found in the provided path (a folder path)

    Args: 
        path (str): This is the path to the folder holding the ical files you want to print
    """

    for path in paths:
        with open(path, 'r') as file:
            calendar = icalendar.Calendar.from_ical(file.read())
            print(f"[blink purple] {calendar["X-WR-CALNAME"]} [/blink purple]")
            for event in calendar.walk('VEVENT'):
                try :
                    summary = event["SUMMARY"]
                    s = event['DTSTART']
                    e = event['DTEND']
                except KeyError as er:
                    print(f'Sorry the key {er} was not found in {summary}\n')
                print_event_details(s, e, summary)

def make_cal() -> icalendar.Calendar:
    """This funtion was for testing on how ot create an ical object
    
    Returns:
    Returns a dummy calander with a title"""
    cal = icalendar.Calendar()
    event = icalendar.Event()
    event.add("SUMMARY", "This is a dummy event")
    cal.add_component(event)
    return cal

def get_cal_paths(path_to_files: str = "./cals") -> list[str]:
    """"
    Gets calender file paths
    
    Args: path_to_files (str) - holds the .ics file path 

    Return: paths (ls) - list of .ics file paths
    """
    paths = []
    try:
        for file_name in os.listdir(path_to_files):
            full_path = f"{path_to_files}/{file_name}"
            paths.append(full_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return paths

def parsing_recurring_events():
    pass


if __name__ == "__main__":
    # # make_cal()
    # # print_cal_info()
    # test_times()
    print_cal_info(get_cal_paths())