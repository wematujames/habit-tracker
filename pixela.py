import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

class Pixela ():
    def __init__(self, **kwargs) -> None:
        if kwargs.get("username"):
            self.username = kwargs.get("username")
        if kwargs.get("token"):
            self.px_auth = {"X-USER-TOKEN": kwargs.get("token")}
        if kwargs.get("graph_id"):
            self.graph_id = kwargs.get("graph_id")


    def create_user (self, username: str, token: str) -> dict:
        body = {
            "token": token, 
            "username": username, 
            "agreeTermsOfService":"yes", 
            "notMinor":"yes"
            }
        res = requests.post(url=PIXELA_ENDPOINT, json=body)
        res.raise_for_status()
        print(res)
        if res.status_code == 200 or res.status_code == 201:
            return {username: body["username"], token: body["token"]}
        else:
            print("Error", res)
            return {}
            

    def create_graph (self, graph_data: dict) -> dict:
        '''Graph data dict: {id: str, name: str, unit: str, type: str, color: str}
        see https://docs.pixe.la/entry/post-graph for more info
        '''
        px_graph = f"{PIXELA_ENDPOINT}/{self.username}/graphs"
        g_res = requests.post(url=px_graph, json=graph_data, headers=self.px_auth)
        g_res.raise_for_status()
        if g_res.status_code == 200 or g_res.status_code == 201:
            return {"graph_id": graph_data.get("id")}
        else:
            print("Error", g_res)
            return {}
    
    
    def post_progress (self, year: int, month: int, day: int, quantity: float) -> None:
        today = datetime(year=year, month=month, day=day)
        today = today.strftime("%Y%m%d")

        post_progress = f"{PIXELA_ENDPOINT}/{self.username}/graphs/{self.graph_id}"
        progress_res = requests.post(url=post_progress, json={"date": today, "quantity": quantity}, headers=self.px_auth)
        progress_res.raise_for_status()


    def update_progress (self, year: int, month: int, day: int, quantity: float) -> None:
        # Update
        day_f = datetime(year=year, month=month, day=day)
        day_f = day_f.strftime("%Y%m%d")
        px_update_url = f"{PIXELA_ENDPOINT}/{self.username}/graphs/{self.graph_id}/{day_f}"
        px_put_res = requests.put(url=px_update_url, headers=self.px_auth, json={"quantity": quantity})
        px_put_res.raise_for_status()
    
    
    def delete_progress (self, year: int, month: int, day: int) -> None:
        del_day = datetime(year=year, month=month, day=day)
        del_day = del_day.strftime("%Y%m%d")
        url  = f"{PIXELA_ENDPOINT}/{self.username}/graphs/{self.graph_id}/{del_day}"
        del_res = requests.delete(url=url, headers=self.px_auth)
        del_res.raise_for_status()
    