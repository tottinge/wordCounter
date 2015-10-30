import unittest
from WordCounter import WordCounter


class TestMe(unittest.TestCase):
    def test_failFast(self):
        sample = "public Album"
        counter = WordCounter()
        counter.count(sample)
        self.assertEqual(1, counter.timesOccurred('public'))

    def test_differentCase(self):
        counter = WordCounter()
        counter.count("Album album ALBUM")
        self.assertEqual(3, counter.timesOccurred('album'))

    def test_counts_words_despite_punctuation(self):
        counter = WordCounter()
        counter.count("Album album = new ALBUM()")
        self.assertEqual(3, counter.timesOccurred('album'))

    def test_counts_a_real_java_sourceline(self):
        sample = """
	private void addOrderEntryLibJars(Tag set) {
		for (String jarName : libJars())
			if (isJunit(jarName))
				addLibraryOrderEntry(set, "junit");
			else
				addLibraryOrderEntry(set, jarName.split(".jar")[0]);
	}"""
        counter = WordCounter()
        counter.count(sample)
        expected = [
                ('jar',4),
                ('set',3),
                ('name',3),
                ('add',3)
        ]
        self.assertEquals(expected, counter.mostUsedWords(4))
        



class TestCamelCase(unittest.TestCase):

    def test_all_lower(self):
        counter = WordCounter()
        result = counter._uncamelCase('this')
        self.assertEquals(['this'], list(result))

    def test_leading_upper(self):
        counter = WordCounter()
        result = counter._uncamelCase('THIS')
        self.assertEquals(['THIS'], list(result))

    def test_capitalized(self):
        counter = WordCounter()
        result = counter._uncamelCase('This')
        self.assertEquals(['This'], list(result))

    def test_joined_leadingLower(self):
        counter = WordCounter()
        result = counter._uncamelCase('thisTime')
        self.assertEquals(['this','Time'], list(result))

    def test_joined_leadingUpper(self):
        counter = WordCounter()
        result = counter._uncamelCase('LeadingUpper')
        self.assertEquals(['Leading','Upper'], list(result))

    def test_end_with_acronym(self):
        counter = WordCounter()
        result = counter._uncamelCase('endWithHTML')
        self.assertEquals(['end','With','HTML'], list(result))

    def test_acronym_in_middle(self):
        counter = WordCounter()
        result = counter._uncamelCase('embedHTMLHere')
        self.assertEquals(['embed','HTML', 'Here'], list(result))




if __name__ == "__main__":
    unittest.main()

