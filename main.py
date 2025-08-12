from rich import print
import icalendar
import datetime

def print_event_details(st: icalendar.Component, et: icalendar.Component):
    start_str = str(st.dt)
    end_str = str(et.dt)
    start_dt = date_time_cons(start_str.split()[0])
    end_dt = date_time_cons(end_str.split()[0])

    print(f'This event starts at {start_dt} and ends at {end_dt}\n')

    print(f'[grey]{type(start_dt)}[/grey]\n')

    print(f'Starts on a {start_dt.strftime("%A")} and ends on a {end_dt.strftime("%A")}\n')

def date_time_cons(dt_str : str) :
    times = dt_str.split('-')
    year = int(times[0])
    month = int(times[1])
    day = int(times[2])
    date = datetime.date(year, month, day)
    return date

def print_cal_info():
    with open('./Cals/personal.ics', 'r') as file:
        calendar = icalendar.Calendar.from_ical(file.read())
        i = 0
        for event in calendar.walk('VEVENT'):
            try :
                s = event['DTSTART']
                e = event['DTEND']
            except KeyError:
                print(f'Sorry the key was not found\n')
            print_event_details(s, e)

def make_cal():
    cal = icalendar.Calendar()
    event = icalendar.Event()
    event.add("SUMMARY", "This is a dummy event")
    cal.add_component(event)
    print(cal)


if __name__ == "__main__":
    make_cal()
    print_cal_info()