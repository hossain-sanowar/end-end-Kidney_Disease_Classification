from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path #these are the access of variable from the other class
    source_URL: str
    local_data_file: Path
    unzip_dir: Path