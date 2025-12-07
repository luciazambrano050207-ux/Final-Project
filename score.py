class Score:
    """ This class represents the score. """

    def __init__(self):
        """ This method creates a Score object. """
        self.__score = 0


    @property
    def score(self) -> int:
        return self.__score


    def __str__(self):
        return str(self.__score)

    def pkg_delivered(self):
        """ This method is called when a package is delivered. It adds 1 to
        the score. """
        self.__score += 1

    def completed_truck(self):
        """ This method is called when a truck is completed. It adds 10 to
        the score. """
        self.__score += 10