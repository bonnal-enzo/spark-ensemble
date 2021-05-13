from pyspark.ml.param import Param, Params


class HasNumBaseLearners(Params):
    """
    param for the number of base learners of the algorithm
    """
    numBaseLearners = Param(Params._dummy(), "numBaseLearners", "number of base learners of the algorithm (>= 1)",
                            typeConverter=TypeConverters.toInt)

    def __init__(self):
        super(HasNumBaseLearners, self).__init__()

    def getNumBaseLearners(self):
        """
        Gets the value of numBaseLearners or its default value.
        """
        return self.getOrDefault(self.numBaseLearners)


class HasBaseLearner(Params):
    """
    param for the estimator that will be used by the ensemble learner as a base learner
    """
    # TODO: how to pass a java class full name or a pyspark Predictor (instead of None)
    baseLearner = Param(Params._dummy(), "baseLearner", "base learner that will be used by the ensemble learner", None)

    def __init__(self):
        super(HasBaseLearner, self).__init__()

    def getBaseLearner(self):
        """
        Gets the value of numBaseLearners or its default value.
        """
        return self.getOrDefault(self.baseLearner)

    # TODO implement additional methods
