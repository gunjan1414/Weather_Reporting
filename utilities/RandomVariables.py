import logging


class RandomVariable:

    @staticmethod
    def variable(var, res):
        try:
            variable_dict = []
            variable_dict[str(var).casefold()] = res
        except Exception as inst:
            logging.info(str(inst))
            pass
