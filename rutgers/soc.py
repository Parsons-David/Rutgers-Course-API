# soc.py

# TODO: ADD ENUMS or constants for levels, campuses, and/or semesters.
import urllib, json


def getJSON(level, campus, semester, subject):

    # TODO: Create validate JSONparam method
    # Syntax Checks

    # Check Level
    if not(level == 'U' or level == 'G'):
        # level is not Undergraduate or Graduate
        print("SOC SYNTAX ERROR: level must be 'U' or 'G'.")

    # Check campus
    if not(campus == 'NB' or campus == 'NK' or campus == 'CM'):
        # campus is not New Brunswick, Newark, or Camden
        print("SOC SYNTAX ERROR: campus must be 'NB', 'NK', or 'CM'.")

    # TODO: Check Semester

    # TODO: Check Subject

    # End Syntax Checks

    # Create URL

    requestURL = 'http://sis.rutgers.edu/soc/courses.json?subject=' + subject +'&semester=' + semester + '&campus=' + campus + '&level=' + level

    response = urllib.urlopen(requestURL).read()
    data = json.loads(response)

    return data


# Representation of SOC Subject
class Subject(object):

    # Constructs new Subject
    def __init__(self, number, JSON):

        # TODO : Determine if the parameter is needed, can be pulled from json
        # Sets course number (ex: "198" - CS, "640" - Math)
        self.number = number
        # Stores json array of courses
        self.json = JSON

        # List of the subject's course objects
        self.courses = []

        # Adds all courses in json to course list
        for c in self.json:
            self.courses.append(Course(c))

    # Returns number of courses offered by subject
    def numCourses(self):
        return len(self.courses)


# TODO : Add all JSON fields
# Representation of SOC Course
class Course(object):

    # Constructs new Course
    def __init__(self, JSON):

        # Stores course number
        self.number = JSON['subject']

        # Stores course title
        self.title = JSON['title']

        # Stores course title
        self.campusCode = JSON['campusCode']

        # List of course's section objects
        self.sections = []

        # Adds all sections in json to section list
        for s in JSON['sections']:
            self.sections.append(Section(s))

        # Stores json object containing Course properties
        self.json = JSON


# TODO : Add all JSON fields
# Representation of SOC Section
class Section(object):

    # Constructs new Section
    def __init__(self, JSON):

        # Stores section index
        self.index = JSON['index']

        # List of section's meetings times
        self.meetings = []

        # Adds all meeting times to section list
        for m in JSON['meetingTimes']:
            self.meetings.append(Meeting(m))


# TODO : Implement generateTime()
# TODO : Add all JSON fields
# Representation of SOC Meeting Time
class Meeting(object):
    # Constructs new Meeting
    def __init__(self, JSON):
        # Stores meeting campus
        self.campus = JSON['campusName']

        # Stores meeting building
        self.building = JSON['buildingCode']

        # Stores meeting room
        self.room = JSON['roomNumber']

        self.startTime = 0
        self.endTime = 0

