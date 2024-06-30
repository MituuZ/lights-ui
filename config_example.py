class Config:
    # Used as the disabled text on the UI and to recognize if a cronjob is disabled
    DISABLED = 'Disabled'
    # Used as the first schedule's name
    SCHEDULE_1 = 'Schedule 1'
    SCHEDULE_1_HOUR = 8
    SCHEDULE_1_MINUTE = 00
    # Used as the second schedule's name
    SCHEDULE_2 = 'Schedule 2'
    SCHEDULE_2_HOUR = 11
    SCHEDULE_2_MINUTE = 00
    # Common description for the schedules, shown on the UI for both
    SCHEDULE_DESCRIPTION = 'Lights go on at: '
    # Site title
    SITE_DESCRIPTION = 'Weekly Schedule'
    # A string that is used to match the cronjob's command to fetch correct jobs
    SCRIPT_IDENTIFIER = 'echo identifiable script snippet'
    # Used to get the cronjob
    USER = 'user'
