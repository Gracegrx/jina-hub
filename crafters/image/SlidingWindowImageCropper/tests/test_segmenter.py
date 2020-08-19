from . import JinaImageTestCase
from .. import SlidingWindowImageCropper


class ImageSegmentTestCase(JinaImageTestCase):

    def test_sliding_windows_no_padding(self):
        img_size = 14
        img_array = self.create_random_img_array(img_size, img_size)
        output_dim = 4
        strides = (6, 6)
        crafter = SlidingWindowImageCropper(target_size=output_dim, strides=strides, padding=False)
        chunks = crafter.craft(img_array)
        self.assertEqual(len(chunks), 4)
        self.assertEqual(chunks[0]['location'], (0, 0))
        self.assertEqual(chunks[1]['location'], (0, 6))
        self.assertEqual(chunks[2]['location'], (6, 0))
        self.assertEqual(chunks[3]['location'], (6, 6))

    def test_sliding_windows_with_padding(self):
        img_size = 14
        img_array = self.create_random_img_array(img_size, img_size)
        output_dim = 4
        strides = (6, 6)
        crafter = SlidingWindowImageCropper(target_size=output_dim, strides=strides, padding=True)
        chunks = crafter.craft(img_array)
        self.assertEqual(len(chunks), 9)
        self.assertEqual(chunks[0]['location'], (0, 0))
        self.assertEqual(chunks[1]['location'], (0, 6))
        self.assertEqual(chunks[2]['location'], (0, 12))
        self.assertEqual(chunks[3]['location'], (6, 0))
        self.assertEqual(chunks[4]['location'], (6, 6))
        self.assertEqual(chunks[5]['location'], (6, 12))
        self.assertEqual(chunks[6]['location'], (12, 0))
        self.assertEqual(chunks[7]['location'], (12, 6))
        self.assertEqual(chunks[8]['location'], (12, 12))

    def test_sliding_windows_without_padding_rectangular_ugly_shapes(self):
        height = 16
        width = 11
        img_array = self.create_random_img_array(img_height=height, img_width=width)
        output_dim = 4
        strides = (4, 4)
        crafter = SlidingWindowImageCropper(target_size=output_dim, strides=strides, padding=False)
        chunks = crafter.craft(img_array)
        self.assertEqual(len(chunks), 8)
        self.assertEqual(chunks[0]['location'], (0, 0))
        self.assertEqual(chunks[1]['location'], (0, 4))
        self.assertEqual(chunks[2]['location'], (4, 0))
        self.assertEqual(chunks[3]['location'], (4, 4))
        self.assertEqual(chunks[4]['location'], (8, 0))
        self.assertEqual(chunks[5]['location'], (8, 4))
        self.assertEqual(chunks[6]['location'], (12, 0))
        self.assertEqual(chunks[7]['location'], (12, 4))
