import pytest
from main import number_doc

doc_test = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

class TestFunction:
    @pytest.mark.parametrize("doc", doc_test)  
    def test_number_doc(self, doc):
      result = number_doc (doc)
      assert result == result
      pass  