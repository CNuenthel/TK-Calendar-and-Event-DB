class Event:
    """
    Models an event object
    """

    """ Year as  integer: 2022 """
    year: int = 0
    """ Month as integer: 1 """
    month: int = 0
    """ Day as integer: 23 """
    day: int = 0
    """ Hours as integer (24-hour clock) """
    time_hours: int = 0
    """ Minutes as integer """
    time_minutes: int or str = "00"
    """ Category for event, such as Work or Therapy """
    category: str = None
    """ Title of event """
    title: str = None
    """ Event details """
    details: str = None
    """ Event Id """
    id: int = None

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def create(kw_dict):
        e = Event()
        for key in kw_dict:
            setattr(e, key, kw_dict[key])
        return e
