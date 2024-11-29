import DocumentCreator
from typing_extensions import Self
class ExcelDocumentCreator(DocumentCreator):
  def __init__(self):
    super().__init__()

  def factory_method(self) -> Document:
    myDocument = DocumentCreator.create_document("Excel")
    print(myDocument.objType)
    self.documents.append(myDocument)
