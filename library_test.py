import unittest
import library

NUM_CORPUS = '''
On the 5th of May every year, Mexicans celebrate Cinco de Mayo. This tradition
began in 1845 (the twenty-second anniversary of the Mexican Revolution), and
is the 1st example of a national independence holiday becoming popular in the
Western Hemisphere. (The Fourth of July didn't see regular celebration in the
US until 15-20 years later.) It is celebrated by 77.9% of the population--
trending toward 80.                                                                
'''


class TestCase(unittest.TestCase):

    # Helper function
    def assert_extract(self, text, extractors, *expected):
        actual = [x[1].group(0) for x in library.scan(text, extractors)]
        self.assertEquals(str(actual), str([x for x in expected]))

    # First unit test; prove that if we scan NUM_CORPUS looking for mixed_ordinals,
    # we find "5th" and "1st".
    def test_mixed_ordinals(self):
        self.assert_extract(NUM_CORPUS, library.mixed_ordinals, '5th', '1st')

    # Second unit test; prove that if we look for integers, we find four of them.
    def test_integers(self):
        self.assert_extract(NUM_CORPUS, library.integers, '1845', '15', '20', '80')

    def test_iso_dates(self):
        self.assert_extract("I was born on 2015-07-25.", library.dates_iso8601, '2015-07-25')

    # Third unit test; prove that if we look for integers where there are none, we get no results.
    def test_no_integers(self):
        self.assert_extract("no integers", library.integers)

    def test_no_dates1(self):
        self.assert_extract("2019-12-32", library.dates_iso8601)

    def test_no_dates2(self):
        self.assert_extract("2019-13-31", library.dates_iso8601)

    def test_human_readable_date01(self):
        self.assert_extract('I was born on 25 Jan 2017.', library.dates_format, '25 Jan 2017')

    def test_human_readable_date02(self):
        self.assert_extract('I was born on 25 Feb 2017.', library.dates_format, '25 Feb 2017')

    def test_human_readable_date03(self):
        self.assert_extract('I was born on 25 Mar 2017.', library.dates_format, '25 Mar 2017')

    def test_human_readable_date04(self):
        self.assert_extract('I was born on 25 Apr 2017.', library.dates_format, '25 Apr 2017')

    def test_human_readable_date05(self):
        self.assert_extract('I was born on 25 May 2017.', library.dates_format, '25 May 2017')

    def test_human_readable_date06(self):
        self.assert_extract('I was born on 25 Jun 2017.', library.dates_format, '25 Jun 2017')

    def test_human_readable_date07(self):
        self.assert_extract('I was born on 25 Jul 2017.', library.dates_format, '25 Jul 2017')

    def test_human_readable_date08(self):
        self.assert_extract('I was born on 25 Aug 2017.', library.dates_format, '25 Aug 2017')

    def test_human_readable_date09(self):
        self.assert_extract('I was born on 25 Sep 2017.', library.dates_format, '25 Sep 2017')

    def test_human_readable_date10(self):
        self.assert_extract('I was born on 25 Oct 2017.', library.dates_format, '25 Oct 2017')

    def test_human_readable_date11(self):
        self.assert_extract('I was born on 25 Nov 2017.', library.dates_format, '25 Nov 2017')

    def test_human_readable_date12(self):
        self.assert_extract('I was born on 25 Dec 2017.', library.dates_format, '25 Dec 2017')


if __name__ == '__main__':
    unittest.main()
