from Products.Five import BrowserView


class Example(BrowserView):
    """Example browserview"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def pageid(self):
        return '-'.join(self.context.getPhysicalPath())[1:]
