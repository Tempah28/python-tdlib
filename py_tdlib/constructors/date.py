from ..factory import Type


class date(Type):
    #  a date according to the Gregorian calendar @day Day
    #  the month, 1-31 @month Month, 1-12 @year Year, 1-9999

    day = None  # type: "int32"
    month = None  # type: "int32"
    year = None  # type: "int32"
