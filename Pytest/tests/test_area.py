import Area


'''test_area file'''

class Test_Area:

    def test_circle(self):
        assert Area.circle(14) == 615.44

    def test_square(self):
        assert Area.square(4) == 16

    def test_rectangle(self):
        assert Area.rectangle(6, 9) == 54

    def test_parallelogram(self):
        assert Area.parallelogram(7, 5) == 35

    def test_triangle(self):
        assert Area.triangle(12, 10) == 60
