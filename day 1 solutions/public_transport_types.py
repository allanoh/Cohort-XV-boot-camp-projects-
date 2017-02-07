
class publictransport(object):
    """
        class used to initiate the various public transport options available"""

    def __init__(self, route=None, fare=500):
        if not isinstance(route, str) and route is not None:
            raise TypeError("route information should be of type string")

        if not isinstance(fare, (float, int, long)):
            raise TypeError("the base fare should be in numerals")

        self.__route = route
        self.__fare = fare

    def set_route(self, route):

        if not isinstance(route, str):
            raise TypeError("route information should be of type string")
        self.__location = location

    def set_fare(self, fare):
        if not isinstance(land_rate, (float, int, long)):
            raise TypeError("the base fare should be in numerals")

        self.__fare = fare

    def get_route(self):
        return self.__route

    def get_fare(self):
        return self.__fare


class ubertaxi(publictransport):
    """This mode of public transport provides for private hire,fare is decided on the distance to be covered"""
    def __init__(self, route=None, distance_=0):

        if not isinstance(distance_, (float, int, long)):
            raise TypeError("Distance should be in KM or Miles input in numerals")

        super(self.__class__, self).__init__(route)
        self.__distance_ = distance_

    def set_fare(self, distance_):
        self.__distance_ = distance_

    def get_distance_(self):
        return self.__distance_

    def get_fare(self):
        return self.__distance_* 60


class minibus(publictransport):
    """
        This mode of transport caters for multiple passangers,fare is based on distance between pickup and dropoff"""
    def __init__(self, route=None, distance_btwn_stop_pick=0):

        if not isinstance(distance_btwn_stop_pick, (float, int, long)):
            raise TypeError("Distance should be in numerals")
        super(self.__class__, self).__init__(route)
        self.__distance_btwn_stop_pick = distance_btwn_stop_pick

    def set_distance_btwn_stop_pick(self, distance_btwn_stop_pick):
        self.__distance_btwn_stop_pick == distance_btwn_stop_pick

    def get_distance_btwn_stop_pick(self):
        return self.__distance_btwn_stop_pick

    def get_fare(self):
        return self.__distance_btwn_stop_pick * 10
