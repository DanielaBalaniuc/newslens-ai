from pathlib import Path
import pandas as pd

NEWS_COLUMNS = [
    "news_id",
    "category",
    "subcategory",
    "title",
    "abstract",
    "url",
    "title_entities",
    "abstract_entities",
]

BEHAVIOR_COLUMNS = [
    "impression_id",
    "user_id",
    "time",
    "history",
    "impressions",
]


class MINDDataLoader:
    """
    Loads the Microsoft MIND dataset.
    """

    def __init__(self, data_dir: str | Path):
        self.data_dir = Path(data_dir)

    def load_news(self) -> pd.DataFrame:
        news = pd.read_csv(
            self.data_dir / "news.tsv",
            sep="\t",
            names=NEWS_COLUMNS,
        )
        return news

    def load_behaviors(self) -> pd.DataFrame:
        behaviors = pd.read_csv(
            self.data_dir / "behaviors.tsv",
            sep="\t",
            names=BEHAVIOR_COLUMNS,
        )
        return behaviors

    def load(self):
        return self.load_news(), self.load_behaviors()
