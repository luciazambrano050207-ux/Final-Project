class Score:
    """ This class represents the score. """
    def __init__(self):
        """ This method creates a Score object. """
        self.score = 0

    def __str__(self):
        return str(self.score)

    def pkg_delivered(self):
        """ This method is called when a package is delivered. It adds 1 to
        the score. """
        self.score += 1

    def completed_truck(self):
        """ This method is called when a truck is completed. It adds 10 to
        the score. """
        self.score += 10