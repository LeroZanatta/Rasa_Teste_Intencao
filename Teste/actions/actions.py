from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionAgradecer(Action):
    def name(self) -> str:
        return "action_agradecer"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Muito obrigado pelo seu feedback!")
        return []

class ActionConfirmarAgendamento(Action):
    def name(self) -> str:
        return "action_confirmar_agendamento"

    def run(self, dispatcher, tracker, domain):
        pessoa = tracker.get_slot("pessoa")
        data = tracker.get_slot("data")
        hora = tracker.get_slot("hora")
        local = tracker.get_slot("local")

        mensagem = f"Consulta confirmada com {pessoa} no {local} para {data} às {hora}."
        dispatcher.utter_message(text=mensagem)
        return []

class ActionCancelarConsulta(Action):
    def name(self) -> str:
        return "action_cancelar_consulta"

    def run(self, dispatcher, tracker, domain):
        pessoa = tracker.get_slot("pessoa")
        local = tracker.get_slot("local")
        
        dispatcher.utter_message(text=f"Sua consulta com {pessoa} na {local} foi cancelada.")
        return [SlotSet("pessoa", None), SlotSet("local", None)]
