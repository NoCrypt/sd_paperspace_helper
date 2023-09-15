import os
from gradio import strings

if os.getenv("PAPERSPACE_FQDN"):
  strings.en["RUNNING_LOCALLY_SEPARATED"] = f"Paperspace Public URL: https://tensorboard-{os.getenv('PAPERSPACE_FQDN')}"

