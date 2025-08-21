from main import get_cal_paths, date_cons, check_time_frame
import icalendar as ics
from rich import print


def get_event_details(cal_paths: list[str]):
    for path in cal_paths:
        with open(path, 'r') as file:
            calendar = ics.Calendar.from_ical(file.read())
            parse_events(calendar)


def parse_events(calendar_to_parse: ics.Calendar):
    events = {}
    count = 0

    for event in calendar_to_parse.walk('VEVENT'):
            print(check_time_frame(event))
    #         count += 1
    #         name = event['SUMMARY']
    #         start_time = str(event.get('DTSTART', '[No Start Date]').dt).split()
    #         end_time = str(event.get('DTEND', '[No End Date]').dt).split()
    #         event_details = {
    #             'name': str(name),
    #             'start_date':  date_cons(start_time[0]),
    #             'end_date':  date_cons(end_time[0]),
    #             'start_time':  '[No Start Time Found]' if len(start_time) == 1 else start_time[1],
    #             'end_time':  '[No End Time Found]' if len(end_time) == 1 else end_time[1],
    #         }
    #         print(f"[blink blue]{start_time}[/blink blue]")
    #         events[f"{calendar_to_parse['X-WR-CALNAME']} Event {count}"] = event_details
    # print(events)




if __name__ == "__main__":
    calanders = get_cal_paths("./TestCals")
    get_event_details(calanders)