from calendar import monthcalendar, monthrange


class DateHandler:
    """ Obtains and organizes routine calendar data """
    year: int
    month: int

    def set_month_year(self, year: int, month: int) -> None:
        """
        Sets month and year

        @Param year 4-digit format year
        @Param month 1-digit format month
        """
        self.year = year
        self.month = month

    def date_list(self) -> list[int]:
        """
        Builds a flattened list of day numbers from a 5-week array
        """
        mc = monthcalendar(self.year, self.month)
        return [date_num for sublist in mc for date_num in sublist]

    @staticmethod
    def month_days(month: int, year: int) -> int:
        """ Returns number of days in a given month/year"""
        return monthrange(year, month)[1]

    @staticmethod
    def month_num_to_string(month: int) -> str:
        """ Dictionary reference for transposing month nums to names """
        month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
                      6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
                      11: "November", 12: "December"}
        return month_dict[month]
