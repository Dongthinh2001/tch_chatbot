
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
DICTS = {
    "giàn phun viên": 500,
    "giàn phun viên nhấp nháy": 650,
    "giàn phun hoa": 300,
    "con sò đổi màu": 400,
    "thác nước bạc": 450,
    "cánh xoay hoa": 680,
    # "Giàn Phun Viên nhấp nháy 2024": 1000,
    # "Giàn Phun Viên đặc biệt 2024": 1200,
    # "Giàn Phun Viên đặc biệt": 800
    }

class ActionCheckPrice(Action):

    def name(self) -> Text:
        return "action_check_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name_product = tracker.get_slot("name")
        name_product = next(tracker.get_latest_entity_values("name"), None)
        print(name_product)
        if name_product:
            dispatcher.utter_message(text=f"Sản phẩm {name_product} có giá {DICTS.get(f'{name_product}')}k")
        else:
            dispatcher.utter_message(text="Xin lỗi! Tôi chưa rõ câu hỏi của bạn!!!")
        return []

class ActionSearchVenues(Action):
    def name(self):
        return "action_search_product"

    def run(self, dispatcher, tracker, domain):
        product = [
            {"name": "Giàn phun viên", "price": 500},
            {"name": "Giàn phun hoa", "price": 400},
            {"name": "Giàn phun hoa", "price": 400},
            {"name": "Giàn phun hoa", "price": 400},
            {"name": "Giàn phun hoa", "price": 400},
            {"name": "Giàn phun hoa", "price": 400},
        ]
        # dispatcher.utter_message(text="here are some products I found")
        description = ", ".join([c["name"] for c in product])
        dispatcher.utter_message(text=f"{description}")
        return []