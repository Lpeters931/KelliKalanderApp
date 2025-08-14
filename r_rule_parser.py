from main import get_cal_paths
from main import date_time_cons
from icalendar import prop
import icalendar as ical
from rich import print
from datetime import datetime

def get_calendars(paths: list[str]) -> list[ical.Calendar]:
    """Gets the clandars from the prodided paths.

    This function will read the .ical files from the provided paths and append them to a list
    which will be returned.

    Args:
        paths (list[str]): list of paths to .ical files.

    Returns:
        list[ical.Calendar]: list of calendar objects from the provided .ical file paths.
    """
    calendars = []
    for path in paths:
        try:
            with open(path, 'r') as file:
                cal = ical.Calendar.from_ical(file.read())
                calendars.append(cal)
        except FileNotFoundError as fnf:
            print(f"File was not found: {fnf}")
    return calendars



def parse_rrule(calendars: list[ical.Calendar]) -> list[ical.Calendar]:
    """Splits the recurring events in the calendars into individual events.
    
    Will iterate through all the calendars in the list provided and return a new list of
    calendar with all the recurring events split into individual events in each calendar.

    Args:
        calendars (list[ical.Calendar]): list of calendars to parse.
        
    Returns:
        list[ical.Calendar]: list of calendars with recurring event split into individual events."""
    
    expanded_calendars = []
    for calendar in calendars:
        for event in calendar.walk('VEVENT'):
            if 'RRULE' in event:
                print(f"This is the event RRULE of {event['SUMMARY']} in {calendar['X-WR-CALNAME']} : [blink blue]{event['RRULE']}[/blink blue]\n")

def seperate_rrule(calendar: ical.Calendar) -> dict:
    """Seperated the recurring events in a calendar into their own calendar.
    
    This will read the calendar for events with RRULE and separate them
    into a python dictionary with the event details needed to seperate the 
    recurring events into their own calendar.
    
    Args:
        calendar (ical.Calendar): calendar event to seperate.
        
    Returns:
        dict: dictionary with the event details from the passed calendar
        event containing an RRULE."""

    nessisary_details = ['SUMMARY', 'DTSTART', 'DTEND']
    events = {}
    count = 0
    for event in calendar.walk('VEVENT'):
        if 'RRULE' in event:
            count += 1
            name = event['SUMMARY']
            start_time = event.get('DTSTART', '[No Start Date]').dt
            end_time = event.get('DTEND', '[No End Date]').dt
            rrule = event['RRULE']
            event_details = {
                'name': str(name),
                'start_time':  date_time_cons(str(start_time).split()[0]),
                'end_time':  date_time_cons(str(end_time).split()[0]),
                'rrule': dict(rrule)
            }
            events[f"{calendar['X-WR-CALNAME']} Event {count}"] = event_details
            print(events)



if __name__ == "__main__":
    # cals = get_calendars(get_cal_paths())
    # parse_rrule(cals)

    with open('./Cals/OwensSChedule.ics', 'r') as file:
        cal = ical.Calendar.from_ical(file.read())
        seperate_rrule(cal)


