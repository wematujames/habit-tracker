from pixela import Pixela
import os

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = os.environ["GRAPH_ID"]

# Pixela instance
pixela = Pixela(graph_id=GRAPH_ID, username=USERNAME, token=TOKEN)

# pixela.post_progress(2022, 4, 12, "52")

# pixela.update_progress(2022, 4, 12, "52")

# pixela.delete_progress(2022, 4, 12)




