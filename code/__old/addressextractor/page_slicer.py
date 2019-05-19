class PageSlicer:

    url = ""

    def __init__(self, u):
        self.url = u



    def encode_slices(self, dl, slices):
        encodings = []
        for sub in slices:
            encodings = dl.get_encodings_for_address(sub)
            encodings.append(2)  # the 2 is the class for a non address string
        return encodings

