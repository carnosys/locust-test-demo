from locust import HttpUser, task, between, tag

class AppUser(HttpUser):
    wait_time = between(1,5)
    weight = 3

  
    def on_start(self):
        with self.client.post("/login", json={"username": "user", "password": "pass"}, catch_response=True) as response:
            if response.json().get("status") != "success":
                print("Unexpected response:", response.json())
            else:
                print("Login successful")
    
    @tag("tag1")
    @task(2)
    def get_item(self):
        item_id = 1
        with self.client.get(f"/item?id={item_id}", catch_response=True) as response:
            if response.status_code != 200:
                print("Failed to get item:", response.text)
            else:
                print("Item retrieved:", response.json())


    @tag("tag2")
    @task(1)
    def hello(self):       
        with self.client.get("/hello", catch_response=True) as response:
            if response.status_code != 200:
                print("Failed to say hello:", response.text)
            else:
                print("Hello response:", response.json())          

    def on_stop(self):
        print("User is stopping")            