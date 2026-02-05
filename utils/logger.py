import logging
import os

def get_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        filename=f"{log_dir}/api.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    return logging.getLogger()
