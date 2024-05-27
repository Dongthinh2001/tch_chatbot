from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCheckPrice(Action):
    def name(self) -> Text:
        return "action_check_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product = tracker.get_slot('product')

        prices = {
            "pháo phun viên": 250,
            "pháo phun hoa": 300,
            "pháo sáng đặc biệt": 400
        }

        price = prices.get(product, "not available")

        if price == "not available":
            dispatcher.utter_message(text=f"Sorry, I don't have the price for {product}.")
        else:
            dispatcher.utter_message(text=f"The price of {product} is {price}$.")

        return [SlotSet("price", price)]
