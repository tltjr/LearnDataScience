class Util:
    def hello(self, x):
        return "hello " + x

    def removeFromAllInSeries(self, series, target):
        return [x.strip(target) for x in series]

    def firstFromRange(self, series):
        return [x.split('-')[0] for x in series]
