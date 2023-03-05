from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) 
class DataIngestionConfig:      #this will also work as a named tuple but is a better way to implement the same concept
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path