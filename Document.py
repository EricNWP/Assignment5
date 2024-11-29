from PDFDocument import PDFDocument
from ExcelDocument import ExcelDocument
from WordDocument import WordDocument
from abc import ABC, abstractmethod
class Document(ABC):

  @staticmethod
  @abstractmethod
  def create() -> None:
    pass
