from src.constants import CREDIT, DEBIT
from src.utils import get_today

TODAY = get_today()
FILE_PATH = "fake_file_path"
FILE_DATA = (
    (TODAY, DEBIT, "111", "descr1"),
    (TODAY, CREDIT, "222", "descr2"),
)
