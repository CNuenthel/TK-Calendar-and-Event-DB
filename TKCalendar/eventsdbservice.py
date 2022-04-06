"""
Houses the EventsDBService class

Dependencies:
    tinydb ~= 4.7.0
"""

from tinydb import TinyDB, Query

from events.events import Event


class EventsDBService:
    """
    Manages event flow in and out of event database
    """
    db = TinyDB

    def __init__(self, db: TinyDB):
        """ Sets tinydb to class attribute """
        self.db = db

    def insert(self, event: Event) -> Event or None:
        """
        Insert an Event to hub_calendar events json

        Parameters:
            event:
                Event object

        Returns:
            Inserted event or none on DB failure
        """
        if event.__dict__ not in self.db.all():
            assigned_id = self.db.insert(event.__dict__)
            setattr(event, "id", assigned_id)
            return event
        else:
            return None

    def find_by_id(self, id: int) -> Event:
        """
        Return an event matching a given ID

        Parameters:
            id:
                Event ID assigned from TinyDB

        Returns:
            Event Object
        """
        return self._marshall(self.db.get(doc_id=id))

    def day_events(self, year: int, month: int, day: int) -> list[Event]:
        """
        Return all events for a specific day

        Parameters:
            year:
                year represented numerically
            month:
                month represented numerically
            day:
                day represented numerically

        Returns:
            Event objects matching a given year, month, day from inside DB
        """
        return [
            self._marshall(event) for event in self.db.all()
            if event["year"] == year and event["month"] == month and event["day"] == day]

    def all_events(self) -> list[Event]:
        """
        Return every event in the DB

        Returns:
            All event data from DB
        """
        return [self._marshall(event) for event in self.db.all()]

    def month_events(self, month: int) -> list[Event]:
        """
        Return all events for a specific month

        Parameters:
            month:
                month represented numerically

        Returns:
            All event data from a selected month
        """
        return [self._marshall(item) for item in self.db.all() if item["month"] == month]

    def remove_event(self, id: int) -> bool:
        """
        Remove event by id from DB

        Parameters:
            id:
                Event ID assigned from TinyDB
        Returns:
            True if success, False if failed
        """
        if self.db.remove(doc_ids=[id]):
            return True
        return False

    def update_event(self, id: int, updating_event: Event) -> bool:
        """
        Update an event by id

        Parameters:
            id:
                Event ID assigned from TinyDB
            updating_event:
                Event object with replacement data

        Returns:
            True if success, False if failed
        """
        z = Query()
        if self.db.update(updating_event.__dict__, z.id == id, [id]):
            return True
        return False

    def clear_events(self):
        """ Clear all events from database """
        self.db.truncate()

    @staticmethod
    def _marshall(event_data):
        """
        Return Event object from json data

        Parameters:
            event_data:
                json dictionary

        """
        event = Event()
        for key in event_data:
            setattr(event, key, event_data[key])
        setattr(event, "id", event_data.doc_id)
        return event
